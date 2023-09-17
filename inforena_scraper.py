import requests
import yaml

from code_parser import CodeParser
from multithreaded_code_writer import MultithreadedCodeWriter
from utils import Utils


class InfoarenaScraper:

    def __init__(self):
        with open("configuration.yaml", "r") as configuration_file:
            configuration_data = yaml.safe_load(configuration_file)

        self.folder_to_be_saved_in = configuration_data["Folder to be saved in"]
        self.session_cookie = configuration_data["Session cookie"]
        self.number_of_entries = configuration_data["Number of entries"]
        self.user_name = configuration_data["User name"]

    def get_problem_page(self, problem_code):
        cookies = {"infoarena2_session": self.session_cookie}
        response = requests.get(f'https://www.infoarena.ro/job_detail/{problem_code}?action=view-source',
                                cookies=cookies)
        return response.text

    def get_source_code(self, problem_code):
        text = self.get_problem_page(problem_code)
        code_parser = CodeParser()
        code_parser.parse_html(text)
        return code_parser.problem_name, code_parser.code[0]

    def get_problems_page(self, first_entry, display_entries):
        response = requests.get(
            f"https://www.infoarena.ro/monitor?user={self.user_name}&display_entries={display_entries}&first_entry={first_entry}")
        return response.text

    def get_name_to_code_map(self, highest_score):
        name_code = {}
        for problem_id in highest_score:
            name, source_code = self.get_source_code(problem_id)
            if name not in name_code:
                name_code[name] = source_code
        return name_code

    def run(self):
        first_entry = 0
        display_entries = 250
        code_writer = MultithreadedCodeWriter()
        while first_entry < self.number_of_entries:
            main_problems_page = self.get_problems_page(first_entry, display_entries)
            problem_ids = Utils.get_problem_ids(main_problems_page)
            highest_score = Utils.get_highest_score_only(problem_ids)
            print(highest_score)
            name_to_code_map = self.get_name_to_code_map(highest_score)
            code_writer.save_source_code_to_files(name_to_code_map, self.folder_to_be_saved_in)
            first_entry += display_entries
        code_writer.shutdown()
