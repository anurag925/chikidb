import logging


def init_logger():
    logging.basicConfig(filename='./logs/app.log',
                        filemode='a',
                        format='%(name)s - %(levelname)s - %(message)s',
                        level=logging.DEBUG)
