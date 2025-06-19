from app import logging

def main(a,b):
    logging.debug('inside the main function')
    return a +b
logging.debug('main function called')
print(main(23,23))