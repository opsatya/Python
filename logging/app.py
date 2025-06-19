import logging


logging.basicConfig(
    level= logging.DEBUG,
    format='%(asctime)s-%(name)s-%(levelname)s-%(message)s',  # Fixed typo: asctime not acstime
    datefmt = '%Y-%m-%d %H:%M:%S',
    handlers=[
        logging.FileHandler("app.log"),
        logging.StreamHandler() # putting all the logs information into the log file

    ]
)


logger = logging.getLogger('ArthmaticApp')


def add(a,b):
    result = a+b
    logger.debug(f'{a} + {b} ,result')
    return result


def sub(a,b):
    result = a-b
    logger.debug(f'{a} - {b} ,result')
    return result


def mul(a,b):
    result = a*b
    logger.debug(f'{a} x {b},result')
    return result


def div(a,b):
    try:        
        result = a/b
        logger.debug(f'{a} / {b} ,result')
        return result
    except ZeroDivisionError:
        logger.error('number cannot divide by the 0')
        return None


print('addition',add(12,23))
print('substraction',sub(12,23))
print('multiplication',mul(12,23))
print('division',div(12,0))