import logging

logging.basicConfig(
    filename='app.log', filemode='w',
    format = '%(name)s - %(asctime)s - %(levelname)s - %(message)s - %(filename)s',
    datefmt='%d-%m-%y %H:%M:%S',
    level=logging.DEBUG,
    )

logging.info('This will get logged from info')
logging.debug('This will get logged from debug')
logging.warning('This will get logged from warning')

name = 'yolov5'
logging.error(f'{name} raised an error')

a = 5
b = 0

try:
    c = a/b
except Exception as e:
    logging.error("Exception occured", exc_info=True)

# add other logger
model_logging = logging.getLogger('model_logger')
model_logging.warning('This is warning from model')