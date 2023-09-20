import requests

from endpoints import SOLUTION_CODE_PAGE_URL, PROBLEMS_PAGE_URL


class InfoarenaRequestHandler:
    def __init__(self, user_name):
        self.__session = requests.session()
        self.__user_name = user_name

    def get_solution_code_page(self, problem_code):
        payload = {
            "force_view_source": "Vezi sursa"
        }
        url = SOLUTION_CODE_PAGE_URL + f'{problem_code}?action=view-source'
        response = self.__session.post(url, data=payload)
        return response.text

    def get_problems_page(self, first_entry, display_entries):
        url = PROBLEMS_PAGE_URL + f"?user={self.__user_name}&display_entries={display_entries}&first_entry={first_entry}"
        response = requests.get(url)
        return response.text
