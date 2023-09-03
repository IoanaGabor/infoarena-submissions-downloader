from html.parser import HTMLParser


class CodeParser(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.code_recording = 0
        self.code = []
        self.problem_name = ""

    def handle_starttag(self, tag, attributes):
        if tag == 'code':
            self.code_recording = 1
        if tag == "a":
            for key, value in attributes:
                if key == "href" and value.startswith("/problema/"):
                    self.problem_name = value[10:]
                    break
                else:
                    return
        return

    def handle_endtag(self, tag):
        if tag == 'code' and self.code_recording:
            self.code_recording -= 1

    def handle_data(self, data):
        if self.code_recording:
            self.code.append(data)
