
import logging

class logGen:
    @staticmethod
    def log_gen():
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)

        file_handler = logging.FileHandler(".\\_Logs\\automation.log")
        formatter = logging.Formatter('%(asctime)s : %(levelname)s : %(message)s',
                                      datefmt='%d/%m/%Y %I:%M:%S %p')
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

        '''
        #logging.basicConfig(filename=".\\_Logs\\automation.log",
        #                    level=logging.INFO, filemode='w',
        #                    format='%(asctime)s:%(levelname)s:%(message)s',
        #                    datefmt='%d/%m/%Y %I:%M:%S %p')
        '''
        return logger

