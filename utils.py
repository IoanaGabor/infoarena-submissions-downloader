from os.path import abspath

from score_and_id_parser import ScoreAndIdParser


class Utils:
    @staticmethod
    def save_code_to_file(code, folder, name):
        path = abspath(f"{folder,}/{name}.cpp")
        print(path)
        fi = open(path, "w")
        fi.writelines(code)
        fi.close()

    @staticmethod
    def get_problem_ids(html_page):
        score_id_parser = ScoreAndIdParser()
        score_id_parser.feed(html_page)
        return score_id_parser.data

    @staticmethod
    def get_highest_score_only(codes):
        highest_score = []
        for code in codes:
            if "100" in code[1]:
                highest_score.append(code[0])
        return highest_score
