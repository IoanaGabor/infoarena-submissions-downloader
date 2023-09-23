import yaml

from exceptions.exceptions import InvalidConfiguration


class Configuration:
    def __init__(self):
        with open("./configuration.yaml", "r") as configuration_file:
            configuration_data = yaml.safe_load(configuration_file)
        self.__folder_to_be_saved_in = configuration_data["Folder to be saved in"]
        self.__number_of_entries_of_a_page = configuration_data["Number of entries of a page"]
        self.__user_name = configuration_data["User name"]
        self.__start_page_index = configuration_data["Start page index"]
        self.__end_page_index = configuration_data["End page index"]
        self.__validate()

    def __validate(self):
        if self.__folder_to_be_saved_in is None:
            raise InvalidConfiguration("No folder to be saved in")
        if self.__number_of_entries_of_a_page is None:
            raise InvalidConfiguration("No number of entries of a page specified")
        if self.__user_name is None:
            raise InvalidConfiguration("No user name specified")
        if self.__start_page_index is None:
            raise InvalidConfiguration("No start page index specified")
        if self.__end_page_index is None:
            raise InvalidConfiguration("No end page index specified")
        if self.__number_of_entries_of_a_page > 250 or self.__number_of_entries_of_a_page < 1:
            raise InvalidConfiguration("Number of entries of a page is above 250 or below 1")
        if self.__start_page_index < 1:
            raise InvalidConfiguration("Start page index should be at least 1")
        if self.__end_page_index < 1:
            raise InvalidConfiguration("End page index should be at least 1")
        if self.__start_page_index > self.__end_page_index:
            raise InvalidConfiguration("Start page index can't be greater than end page index")

    @property
    def user_name(self):
        return self.__user_name

    @property
    def number_of_entries_of_a_page(self):
        return self.__number_of_entries_of_a_page

    @property
    def folder_to_be_saved_in(self):
        return self.__folder_to_be_saved_in

    @property
    def start_page_index(self):
        return self.__start_page_index

    @property
    def end_page_index(self):
        return self.__end_page_index
