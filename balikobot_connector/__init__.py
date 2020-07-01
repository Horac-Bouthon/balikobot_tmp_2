from conf.settings_wrapper import SettingsWrapper

SETTING_CONTAINER = SettingsWrapper()
SETTING_CONTAINER.read_data()
LOGGER_MAIN_NAME = SETTING_CONTAINER.settings_local['LOGGER_NAME']
