# from Modules.setup_logger import setup_logger
import pandas as pd
import json
from setup_logger import setup_logger


class DataGetter:
    """
    Class for loading data from local and saving data to local
    """

    def __init__(self):

        # setting up a logger
        self.log = setup_logger(logger_name="DataGetter_Log",  log_file="./logs/DataGetter.log")

        self.data_path = "./jalandhar_zomato.csv"

    def data_getter(self, data_path):
        """
        Method: data_getter
        Description: loading csv data from local and return pandas dataframe

        Input: data_path
        Output: Pandas dataframe

        On Error: log error and raise error
        """
        try:
            self.log.info("Loading the data csv file from local system...data_getter successful")
            data = pd.read_csv(data_path)
            self.log.info("Data load from system successfully...")
            print("hi")
            print(data)
            return data  # return pandas dataframe.

        except Exception as e:
            self.log.error("Error on Loading data......data_getter failed")
            raise e

    def data_saved(self, data, data_path):
        """
        Method: data_saved
        Description: saving the data to local

        Input: data_path: we input the data_path to save the data
                        : data: data to save as pandas dataframe
        Output: Saved csv file to preferred location...."*.csv" file

        On Error: Raise log error and raise error
        """
        try:
            self.log.info("Saving the data to local...")
            data.to_csv(data_path, index=False)  # saving the data to local
            self.log.info("Data saved successfully")
        except Exception as e:
            self.log.error("Error on Saving data")
            raise e

    def save_json(self, label_encoding_dict, file_name):
        """
        Method: save_json
        Description: This method will save dictionary as json file
        Input: dict_: (dict) dictionary to be saved
        Output: None

        On Error: log and raise error.
        """
        try:
            self.log.info("save_json Started")
            with open(file_name, 'w+') as f:
                json.dump(label_encoding_dict, f, indent=4)  # dumping dictionary as json file
            self.log.info("save_json Completed")
        except Exception as e:
            self.log.error("Error occured in save_json " + str(e))
            raise Exception("Error occured in save_json " + str(e))

    def load_json(self, file_name):
        """
        Method: load_json
        Description: It will load dictionary from json file which we saved using save_json method
        Input: file_name: (str) name of the json file
        Output: (dict) dictionary loaded from json file

        On Error: raise error, log Error.
        """
        try:
            self.log.info("Loading dictionary from json file")
            with open(file_name, 'r') as f:
                dict_ = json.load(f)  # loading dictionary from json file
            self.log.info("Dictionary loaded from json file")
            return dict_
        except Exception as e:
            self.log.error("Error occured while loading dictionary from json file " + str(e))
            raise Exception("Error occured while loading dictionary from json file " + str(e))
