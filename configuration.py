import yaml

from exceptions import InvalidConfiguration


class Configuration:
    def __init__(self):
        with open("configuration.yaml", "r") as configuration_file:
            configuration_data = yaml.safe_load(configuration_file)
        self.__folder_to_be_saved_in = configuration_data["Folder to be saved in"]
        self.__number_of_entries = configuration_data["Number of entries"]
        self.__user_name = configuration_data["User name"]
        self.__validate()

    def __validate(self):
        if self.__folder_to_be_saved_in is None:
            raise InvalidConfiguration("No folder to be saved in")
        if self.__number_of_entries is None:
            raise InvalidConfiguration("No maximum number of entries specified")
        if self.__user_name is None:
            raise InvalidConfiguration("No user name specified")

    @property
    def user_name(self):
        return self.__user_name

    @property
    def number_of_entries(self):
        return self.__number_of_entries

    @property
    def folder_to_be_saved_in(self):
        return self.__folder_to_be_saved_in
