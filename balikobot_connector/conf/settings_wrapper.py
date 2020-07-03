from . import (
    settings,
    settings_local,
)

from logger_wrapper import LOGGER_NAME as lw_logger_name
from logger_wrapper import LOG_FILE as lw_log_file
from logger_wrapper import LOG_LEVEL as lw_logg_level
import logging


if hasattr(settings, 'LOGGER_NAME'):
    LOGGER_MAIN_NAME = settings.LOGGER_NAME
else:
    LOGGER_MAIN_NAME = lw_logger_name
local_name = LOGGER_MAIN_NAME + '.' + __name__

class SettingsWrapper:
    """ Class to wrap settings and set values if there are not valid settings. """

    def __init__(self):
        """ Wrapper constructor """
        self.logger = logging.getLogger(local_name)
        self.settings = dict()
        self.settings_local = dict()
        self.logger.debug('Create: {}'.format(repr(self)))

    def set_entry(
            self,
            par_object,
            target_dic,
            atr_name: str,
            def_value = 'NOP',
    ):
        """ one attribute handler """
        if hasattr(par_object, atr_name):
            set_value = getattr(par_object, atr_name)
            ret_val = set_value
        else:
            ret_val = def_value
        target_dic[atr_name] = ret_val
        return ret_val

    def read_data(self):
        """ Reads from data to inner dictionaries """

        self.logger.debug('add data to settings=> HOST: ()'.format(self.set_entry(
            par_object=settings,
            target_dic=self.settings,
            atr_name='HOST',
            def_value='0.0.0.0',
        )))
        self.logger.debug('add data to settings=> PORT: ()'.format(self.set_entry(
            par_object=settings,
            target_dic=self.settings,
            atr_name='PORT',
            def_value=8000,
        )))
        self.logger.debug('add data to settings=> API_TITLE: ()'.format(self.set_entry(
            par_object=settings,
            target_dic=self.settings,
            atr_name='API_TITLE',
            def_value='API title',
        )))
        self.logger.debug('add data to settings=> API_DESCRIPTION: ()'.format(self.set_entry(
            par_object=settings,
            target_dic=self.settings,
            atr_name='API_DESCRIPTION',
            def_value='Some simple description for the API',
        )))
        self.logger.debug('add data to settings=> API_MAIN_VERSION: ()'.format(self.set_entry(
            par_object=settings,
            target_dic=self.settings,
            atr_name='API_MAIN_VERSION',
            def_value='0.0.1',
        )))
        self.logger.debug('add data to settings=> API_SUPER_SECRET_TOKEN: ()'.format(self.set_entry(
            par_object=settings,
            target_dic=self.settings,
            atr_name='API_SUPER_SECRET_TOKEN',
            def_value='SuPeR_SeCrEd_TOKEN',
        )))

        # -------- local settings
        self.logger.debug('add data to local settings=> LOGGER_NAME: ()'.format(self.set_entry(
            par_object=settings_local,
            target_dic=self.settings_local,
            atr_name='LOGGER_NAME',
            def_value=lw_logger_name,
        )))
        self.logger.debug('add data to local settings=> LOGGER_FILE: ()'.format(self.set_entry(
            par_object=settings_local,
            target_dic=self.settings_local,
            atr_name='LOGGER_FILE',
            def_value=lw_log_file,
        )))
        self.logger.debug('add data to local settings=> LOG_LEVEL: ()'.format(self.set_entry(
            par_object=settings_local,
            target_dic=self.settings_local,
            atr_name='LOG_LEVEL',
            def_value=lw_logg_level,
        )))
        self.logger.debug('add data to local settings=> LTECH_FILE: ()'.format(self.set_entry(
            par_object=settings_local,
            target_dic=self.settings_local,
            atr_name='LTECH_FILE',
            def_value=lw_log_file,
        )))
        self.logger.debug('add data to local settings=> LTECH_LEVEL: ()'.format(self.set_entry(
            par_object=settings_local,
            target_dic=self.settings_local,
            atr_name='LTECH_LEVEL',
            def_value=lw_logg_level,
        )))
        self.logger.debug('add data to local settings=> SQLALCHEMY_DATABASE_TYPE: ()'.format(self.set_entry(
            par_object=settings_local,
            target_dic=self.settings_local,
            atr_name='SQLALCHEMY_DATABASE_TYPE',
            def_value='SQLITE',
        )))
        self.logger.debug('add data to local settings=> SQLALCHEMY_DATABASE_URL: ()'.format(self.set_entry(
            par_object=settings_local,
            target_dic=self.settings_local,
            atr_name='SQLALCHEMY_DATABASE_URL',
            def_value='sqlite:///./sql_balikobot.db',
        )))
        return

    def get_logger_name(self, postfix: str) -> str:
        return '{}.{}'.format(self.settings_local['LOGGER_NAME'], postfix)

    def __repr__(self):
        return 'SettingsWrapper()'

    def __str__(self):
        return self.file_name


