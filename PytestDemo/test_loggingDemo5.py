import logging

def test_loggingDemo():
    logger = logging.getLogger(__name__)
    fileHandler = logging.FileHandler("loggingDemofile.log")

    formatter = logging.Formatter("%(asctime)s :: %(levelname)s :: %(name)s :: %(message)s")
    fileHandler.setFormatter(formatter)

    logger.addHandler(fileHandler)

    logger.setLevel(logging.INFO)

    logger.info("This is a test info message")
    logger.debug("This is a test debug message")
    logger.warning("This is a test warning message")
    logger.error("This is a test error message")
    logger.critical("This is a test critical message")