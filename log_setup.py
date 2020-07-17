import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# create a file handler
handler = logging.FileHandler('pycon.log')
handler.setLevel(logging.INFO)

# create a logging format
format_str = '[%(asctime)s] {%(pathname)s:%(lineno)d} %(levelname)s - %(message)s'
formatter = logging.Formatter(format_str)
handler.setFormatter(formatter)

# add the handler to the logger
logger.addHandler(handler)


