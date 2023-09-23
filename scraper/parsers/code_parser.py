from bs4 import BeautifulSoup


class CodeParser:
    def __init__(self):
        self.soup = None
        self.code = []
        self.problem_name = ""

    def parse_html(self, html_content):
        self.soup = BeautifulSoup(html_content, 'html.parser')
        self.code = []
        self.problem_name = ""
        self._parse_code()

    def _parse_code(self):
        code_tags = self.soup.find_all('code')
        for code_tag in code_tags:
            self.code.append(code_tag.text)

        problem_link = self.soup.find('a', href=lambda x: x and x.startswith("/problema/"))
        if problem_link:
            self.problem_name = problem_link['href'][10:]
