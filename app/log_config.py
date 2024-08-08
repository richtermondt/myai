import logging


def configure_logging():
    logging.basicConfig(level=logging.DEBUG)
    file_handler = logging.FileHandler('app.log')
    file_handler.setLevel(logging.DEBUG)
    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(formatter)
    logging.getLogger().addHandler(file_handler)
