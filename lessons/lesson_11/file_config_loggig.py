from constants import BASE_PATH
import os
import logging.config
import logging


config_file_path = os.path.join(BASE_PATH, 'log_config.ini')   #  BASE_PATH + log_config.ini з правильним слешем
logging.config.fileConfig(config_file_path)  # звідки брати файл конфігурації

# Використання логера
logger = logging.getLogger('sampleLogger')
new_logger = logging.getLogger('customLogger')

logger.debug('Це повідомлення рівня DEBUG')
logger.info('Це повідомлення рівня INFO')
logger.critical('Це повідомлення рівня CRITICAL')


new_logger.debug('new_logger: debug message')
new_logger.warning('new_logger: warning message')