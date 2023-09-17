from bs4 import BeautifulSoup


class ScoreAndIdParser:
    def __init__(self):
        self.soup = None
        self.data = []

    @staticmethod
    def get_problem_id_from_link(link):
        tokens = link.split('?')
        return tokens[0][12:]

    def parse_html(self, html_content):
        self.soup = BeautifulSoup(html_content, 'html.parser')
        self.data = []
        self._parse_table()

    def _parse_table(self):
        table = self.soup.find('tbody')
        if table:
            for link in table.find_all('a', href=True):
                problem_id = self.get_problem_id_from_link(link['href'])
                self.current_problem_id = problem_id
                self._parse_problem_status(link)

    def _parse_problem_status(self, link):
        status_span = link.find('span', class_='job-status-done')
        if status_span:
            self.data.append((self.current_problem_id, status_span.text))
