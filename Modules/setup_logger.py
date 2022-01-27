import logging

log_format = '%(asctime)s - %(levelname)s - %(funcName)s - %(message)s'

formatter = logging.Formatter(log_format)

def setup_logger(logger_name='my_log', log_file='my_log.log', level=logging.DEBUG, log_format = formatter):
    ''' 
        Used for creating logging in the application for
        monitoring the application flow step by step.
    '''
    handler = logging.FileHandler(log_file)  #adding log file to file handler
    handler.setFormatter(log_format)         # setting the format for the logger

    logger = logging.getLogger(logger_name)  #creating the main logger
    logger.setLevel(level)                   #setting the logger level
    logger.addHandler(handler)               # adding the logger to file handler

    return logger                           #returning the logger


# #giving the msg
# log_1.info('THis is from log1')
# log_2.info('thia ia from log2')