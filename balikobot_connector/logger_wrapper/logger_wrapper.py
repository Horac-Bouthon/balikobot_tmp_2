import logging
import logging.handlers
from . import LOG_LEVEL, LOG_FILE, MAX_BYTES, MAX_COUNT
import os


class LoggerWrapper:

    @staticmethod
    def set_logger(
            logger,
            log_ex=None,
            verbose=False,
            log_level=None,
            console=True,
    ):
        """ set basic logger operational """
        return_val = logger
        if log_level is not None:
            str_level = log_level
        else:
            str_level = LOG_LEVEL
        level = logging.ERROR
        if 'WARNING' in str_level:
            level = logging.WARNING
        if 'INFO' in str_level:
            level = logging.INFO
        if 'DEBUG' in str_level:
            level = logging.DEBUG
        return_val.setLevel(level)
        if log_ex:
            folder = log_ex
        else:
            folder = LOG_FILE
        # check end create folder
        dir_tc = os.path.dirname(os.path.abspath(folder))
        if not os.path.isdir(dir_tc):
            os.mkdir(dir_tc)
        max_bytes = MAX_BYTES
        if max_bytes < 1024:
            max_bytes = 1024
        max_count = MAX_COUNT
        if max_count < 1 or max_count > 10:
            max_count = 10
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        fh = logging.handlers.RotatingFileHandler(folder, maxBytes=max_bytes, backupCount=max_count)
        fh.setLevel(level)
        fh.setFormatter(formatter)
        return_val.addHandler(fh)
        if console:
            ch = logging.StreamHandler()
            if verbose:
                ch.setLevel(logging.INFO)
            else:
                ch.setLevel(level)
            ch.setFormatter(formatter)
            return_val.addHandler(ch)
        return return_val

    def create_tech_handler(
            self,
            log_file: str,
            log_level: str,
    ):
        if log_level is not None:
            str_level = log_level
        else:
            str_level = LOG_LEVEL
        level = logging.ERROR
        if 'WARNING' in str_level:
            level = logging.WARNING
        if 'INFO' in str_level:
            level = logging.INFO
        if 'DEBUG' in str_level:
            level = logging.DEBUG
        if log_file:
            folder = log_file
        else:
            folder = LOG_FILE
        # check end create folder
        dir_tc = os.path.dirname(os.path.abspath(folder))
        if not os.path.isdir(dir_tc):
            os.mkdir(dir_tc)
        max_bytes = MAX_BYTES
        if max_bytes < 1024:
            max_bytes = 1024
        max_count = MAX_COUNT
        if max_count < 1 or max_count > 10:
            max_count = 10
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        new_handler = logging.handlers.RotatingFileHandler(folder, maxBytes=max_bytes, backupCount=max_count)
        new_handler.setLevel(level)
        new_handler.setFormatter(formatter)
        return new_handler

    def __init__(self):
        return

    def __repr__(self):
        return "LoggerWrapper()"

    def __str__(self):
        return 'LoggerWrapper'
