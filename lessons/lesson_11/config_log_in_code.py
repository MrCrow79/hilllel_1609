import logging

f_handler = logging.FileHandler('error.log')
my_format = logging.Formatter('!!!!! %(asctime)s - %(name)s -  %(levelname)s - %(message)s:  ' )

f_handler.setLevel(logging.ERROR)
f_handler.setFormatter(my_format)

# Створення конфігурації
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s -  %(levelname)s - %(message)s',
                    handlers=[
                        logging.StreamHandler(),  # Виведення в консоль
                        logging.FileHandler('example.log') , # Запис у файл
                        f_handler  # Запис у файл
                    ])

# Використання логера
logger = logging.getLogger('my_logger')

logger.debug('Це повідомлення рівня DEBUG')
logger.info('Це повідомлення рівня INFO')
logger.error('Це повідомлення рівня ERROR')
