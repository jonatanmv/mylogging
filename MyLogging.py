import datetime
import os
from pathlib import Path

import logging
import logging.handlers
from logging.config import fileConfig


class MyLog(object):

    # Logging destinations defaults
    LOG_TO_CONSOLE = True
    LOG_TO_FILE = True
    LOG_FOLDER = 'logfiles'
    NAME = __name__ # Output file will be 'yyyymmdd_NAME.log'

    # Logging Format
    log_level = logging.DEBUG
    LOG_FORMAT = "{asctime} [{levelname:5s}] [{name}] {filename:s}:{lineno:d} {message:s}"
    LOG_DATE_FORMAT = '%Y-%m-%d %H:%m'
    LOG_FORMATTER = logging.Formatter(
        LOG_FORMAT,
        datefmt=LOG_DATE_FORMAT,
        style='{'
    )

    def get_logger(
        name=NAME,
        log_to_console=LOG_TO_CONSOLE,
        log_to_file=LOG_TO_FILE,
        log_folder=LOG_FOLDER,
        log_level = logging.DEBUG,
        log_format = LOG_FORMAT,
        log_formatter = LOG_FORMATTER,
        log_date_format = LOG_DATE_FORMAT,
    ):

        # Logging basic config
        TIMESTAMP = datetime.datetime.today().strftime('%Y%m%d')
        if log_to_file:
            if not os.path.exists(log_folder):
                os.makedirs(log_folder)
            log_filename = os.path.join(log_folder,TIMESTAMP+"_"+Path(name).with_suffix('').stem)
            log_filename += ".log"
        if log_to_console:
            print("Logging to console...")
            logging.basicConfig(
                format=log_format,
                style="{",
                datefmt=log_date_format,
                level=log_level,
            )
            if log_to_file:
                print(f'Logging to file... {log_filename}')
                fileHandler = logging.handlers.RotatingFileHandler(log_filename, maxBytes=(1048576*5), backupCount=7)
                fileHandler.setFormatter(log_formatter)
                fileHandler.setLevel(log_level)
        elif log_to_file:
            print(f'Logging to file... {log_filename}')
            logging.basicConfig(
                filename=log_filename,
                format=log_format,
                style="{",
                datefmt=log_date_format,
                level=log_level
            )

        # Log
        log = logging.getLogger()
        if log_to_console and log_to_file:
            log.addHandler(fileHandler)

        return log