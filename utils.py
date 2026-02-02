import logging

logging.basicConfig(
    level = logging.INFO,
    format = '%(asctime)s - %(levelname)s - %(message)s',
    filename = 'app.log',
    filemode = 'a'
)

def log_error(pesan):
    logging.error(pesan)

def log_info(pesan):
    logging.info(pesan)