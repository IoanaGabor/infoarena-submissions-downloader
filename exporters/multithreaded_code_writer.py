import concurrent.futures
from os.path import abspath


class MultithreadedCodeWriter:

    def __init__(self):
        self.thread_pool = concurrent.futures.ThreadPoolExecutor(max_workers=4)

    def save_source_code_to_files(self, name_code, folder_to_be_saved_in):
        for name in name_code.keys():
            code = name_code[name]
            self.thread_pool.submit(MultithreadedCodeWriter.save_code_to_file, code, folder_to_be_saved_in, name)

    @staticmethod
    def save_code_to_file(code, folder, name):
        path = abspath(f"{folder}/{name}.cpp")
        fi = open(path, "w")
        fi.writelines(code)
        fi.close()

    def shutdown(self):
        self.thread_pool.shutdown(wait=True)
