import logging


class LoggerUtils:
    @staticmethod
    def set_up_logger():
        logger = logging.getLogger('logger')
        logger.setLevel(logging.INFO)
        consoleHandler = logging.StreamHandler()
        consoleHandler.setLevel(logging.INFO)
        logger.addHandler(consoleHandler)
        return logger
