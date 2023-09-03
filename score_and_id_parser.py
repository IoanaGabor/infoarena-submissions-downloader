from html.parser import HTMLParser


class ScoreAndIdParser(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.recording = 0
        self.table = 0
        self.data = []
        self.problem_link = 0
        self.current_problem_id = -1

    @staticmethod
    def get_problem_id_from_link(link):
        tokens = link.split('?')
        return tokens[0][12:]

    def handle_starttag(self, tag, attributes):
        if tag == 'tbody':
            self.table = 1
            return
        if self.table and tag == "a":
            for name, value in attributes:
                if name == "href" and value.startswith("/job_detail/"):
                    break
                else:
                    return
            self.current_problem_id = ScoreAndIdParser.get_problem_id_from_link(attributes[0][1])

        if self.table and self.current_problem_id and tag == "span":
            for name, value in attributes:
                if name == "class" and value == "job-status-done":
                    break
                else:
                    return
            self.recording = 1

    def handle_endtag(self, tag):
        if tag == 'tbody' and self.table:
            self.table = 0
            return
        if self.table and tag == 'a' and self.current_problem_id != 0:
            self.current_problem_id = 0
        if tag == 'span' and self.recording:
            self.recording = 0

    def handle_data(self, data):
        if self.recording:
            self.data.append((self.current_problem_id, data))
