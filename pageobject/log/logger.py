# _*_ coding=utf-8 _*_
# __author__ = 'lucas'
import logging


class Logging(object):

    def __init__(self, level=logging.DEBUG, out_format='%(asctime)s [line:%(lineno)d] %(message)s',
                 datefmt='%a, %d %b %Y %H:%M:%S',
                 filename='/Users/lucas/PycharmProjects/PageObjects/pageobject/mytest.log', filemode='w'):
        self.level = level
        self.format = out_format
        self.datefmt = datefmt
        self.filename = filename
        self.filemod = filemode
        self.basic_config()

    def basic_config(self):
        logging.basicConfig(level=self.level,
                            format=self.format,
                            datefmt=self.datefmt,
                            filemode=self.filemod,
                            filename=self.filename)

    def write(self, msg, level="info"):

        if level.lower() == "info":
            logging.info(msg)
        elif level.lower() == "debug":
            logging.debug(msg)
        elif level.lower() == "error":
            logging.error(msg)
        elif level.lower() == "warning":
            logging.warning(msg)
        elif level.lower() == "critical":
            logging.critical(msg)

