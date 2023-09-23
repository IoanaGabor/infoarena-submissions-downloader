from scraper.parsers.code_parser import CodeParser
from utils.configuration import Configuration
from request_handling.infoarena_request_handler import InfoarenaRequestHandler
from exporters.multithreaded_code_writer import MultithreadedCodeWriter
from utils.utils import Utils


class InfoarenaScraper:

    def __init__(self, configuration: Configuration, logger):
        self.folder_to_be_saved_in = configuration.folder_to_be_saved_in
        self.user_name = configuration.user_name
        self.number_of_entries_of_a_page = configuration.number_of_entries_of_a_page
        self.start_page_index = configuration.start_page_index
        self.end_page_index = configuration.end_page_index
        self.request_handler = InfoarenaRequestHandler(self.user_name)
        self.logger = logger

    def get_solution_code(self, problem_code):
        text = self.request_handler.get_solution_code_page(problem_code)
        code_parser = CodeParser()
        code_parser.parse_html(text)
        return code_parser.problem_name, code_parser.code[0]

    def get_name_to_code_map(self, highest_score):
        name_code = {}
        for problem_id in highest_score:
            name, source_code = self.get_solution_code(problem_id)
            if name not in name_code:
                name_code[name] = source_code
        return name_code

    def run(self):
        first_entry = (self.start_page_index - 1) * self.number_of_entries_of_a_page
        code_writer = MultithreadedCodeWriter()
        number_of_correct_submissions = 0
        number_of_pages = self.end_page_index - self.start_page_index + 1
        for _ in range(number_of_pages):
            main_problems_page = self.request_handler.get_problems_page(first_entry, self.number_of_entries_of_a_page)
            self.logger.info(
                "processing entries between {0} and {1} ...".format(first_entry,
                                                                    first_entry + self.number_of_entries_of_a_page - 1))
            problem_ids = Utils.get_problem_ids(main_problems_page)
            highest_score = Utils.get_correct_submissions_only(problem_ids)
            self.logger.info("{0} problems with correct submission found".format(len(highest_score)))
            name_to_code_map = self.get_name_to_code_map(highest_score)
            code_writer.save_source_code_to_files(name_to_code_map, self.folder_to_be_saved_in)
            first_entry += self.number_of_entries_of_a_page
            number_of_correct_submissions += len(highest_score)
        code_writer.shutdown()
        self.logger.info("{0} problems with correct submission processed".format(number_of_correct_submissions))
