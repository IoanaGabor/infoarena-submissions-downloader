from configuration import Configuration
from inforena_scraper import InfoarenaScraper
from log import LoggerUtils

if __name__ == "__main__":
    logger = LoggerUtils.set_up_logger()
    try:
        configuration = Configuration()
        inforena_scraper = InfoarenaScraper(configuration, logger)
        inforena_scraper.run()
    except Exception as e:
        logger.error("An error occurred: {0}".format(str(e)))
