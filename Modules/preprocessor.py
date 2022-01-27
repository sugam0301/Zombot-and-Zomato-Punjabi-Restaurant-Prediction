# from Modules.setup_logger import setup_logger
# from Modules.data_loader import DataGetter
# from Modules.data_transformation import DataTransformation
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from statsmodels.stats.outliers_influence import variance_inflation_factor

from data_loader import DataGetter
from data_transformation import DataTransformation
from setup_logger import setup_logger


# Methods
# 1. drop_columns
# 2. fill_na
# 3. check_vif
# 4. drop_null
# 5. drop_duplicates
# 6. label_encoding

class Preprocessor():
    """
    Class for preprocessing the data
    Description: This class contain all necessary method to preprocess the data.
    return: Preprocessed data saved on local

    """
    def __init__(self):
        self.log = setup_logger("preprocessor_log", "logs/preprocessor.log") # logger
        self.data_getter = DataGetter() # data getter object
        self.data_transformation = DataTransformation() # data transformation object



    def drop_columns(self, data, col_list):
        """
            Method: drop_columns

            Descriptions: this method will passed column from data

            Input: data: pandas dataframe
                   col_list: list of columns to be dropped

            Output: data: pandas dataframe after dropping columns

            On error: raise error, log error on log files
        """
        try:
            self.log.info("Dropping columns from data")
            data.drop(col_list, axis=1, inplace=True) # drop columns with inplace True, for reflecting on original data
            self.log.info("Columns dropped successfully")
            return data # returns data after dropping columns

        except Exception as e:
            self.log.error("Error occured while dropping columns from data " + str(e))
            raise Exception("Error occured while dropping columns from data " + str(e))

    def fill_na(self, data, col):
        """
            Method: fillna

            Descriptions: this method will passed column from data

            Input: data: pandas dataframe
                   fillna

            Output: data: pandas dataframe after dropping columns

            On error: raise error, log error on log files
        """
        try:
            self.log.info("Fillna started")
            data[col] = data[col].fillna(data[col].mean())
            data[col] = data[col].replace(0,data[col].mean())

            self.log.info("Columns fillna successfully")
            return data # returns data after dropping columns

        except Exception as e:
            self.log.error("Error occured while filling columns in data " + str(e))
            raise Exception("Error occured while filling columns in data " + str(e))



    def check_vif(self, data):
        """
        Methode: check_vif
        Description: This method will check VIF(Variance Inflation_factor) on data
                    and will drop those columns have VIF value above predefined threshold
        Input: data: pandas dataframe
        Output: data: pandas dataframe after removing columns if VIF value is above threshold for columns.
        
        On error: raise error, log error on log files
        """
        try:
            self.log.info("Checking VIF on data")
            vif = pd.DataFrame() # create empty dataframe to store vif values
            vif["VIF Factor"] = [variance_inflation_factor(data.values, i) for i in range(data.shape[1])]
                                                                                    # calculate vif values
            vif["features"] = data.columns # add column name to dataframe
            self.log.info("VIF DataFrame Created")

            # remove columns with vif value above threshold
            threshold = 5.0 # can be varied.
            vif_filter = vif[vif["VIF Factor"] < threshold] # filtering dataframe with vif value less than threshold
            col_to_drop = vif_filter["features"].tolist() # list of columns to be dropped
            data = self.drop_columns(data, col_to_drop) # droping columns from data
            self.log.info("VIF checked successfully")
            return data # return data after removing columns

        except Exception as e:
            self.log.error("Error occured while checking VIF on data " + str(e))

            raise Exception("Error occured while checking VIF on data " + str(e))


    def drop_null(self, data):
        """
        Method: drop_null
        Descriptions: this method will drop null values from data

        Input: data: pandas dataframe
        Output: data: pandas dataframe after dropping null values
        
        On error: raise error, log error on log files

        """
        try:
            self.log.info("Dropping null values from data")
            data.dropna(inplace=True) # drop null values with inplace True, for reflecting on original data
            self.log.info("Null values dropped successfully")
            return data # return data after dropping null values

        except Exception as e:
            self.log.error("Error occured while dropping null values from data " + str(e))
            raise Exception("Error occured while dropping null values from data " + str(e))

    
    def drop_duplicates(self, data):
        """
        Method: drop_duplicate

        Descriptions: this method will drop duplicate values from data
        Here , it means that if 2 rows are same exactly, then we remove that redundant part of the dataset.
        Return DataFrame with duplicate rows removed.
        Considering certain columns is optional. Indexes, including time indexes are ignored.

        Input: data: pandas dataframe
        Output: data: pandas dataframe after dropping duplicate values
        
        On error: raise error, log error on log files
        """
        try:
            self.log.info("Dropping duplicate values from data")
            data.drop_duplicates(inplace=True) # drop duplicate values with inplace True
                                              # inplace is used to avoid copy of data and same dataset is returned
            self.log.info("Duplicate values dropped successfully")
            return data  #return data after dropping duplicate values from the dataset

        except Exception as e:
            self.log.error("Error occured while dropping duplicate values from data " + str(e))
            raise Exception("Error occured while dropping duplicate values from data " + str(e))



    def label_encoding(self, data, cat_col):
        """
        Method: label_encoding
        Description: This methode will use sklearn LabelEncoder
                    to encoding categorical features.
                    also it will store encoding label with respective feature label.
                    Encode target labels with value between 0 and no of classes - 1.
                    This fxn should be used to encode target values, that is y not the input X.
                    Because the machine learning model will not be able to rectify string values.


        Input: data: pandas dataframe.
                cat_col: (str) single categorical feature column name
        Output: data: pandas dataframe after encoding categorical features.
                label_encode_dict: (dict) dictionary of label encoding with respective feature label.
        On Error: raise error, log Error.
        """
        try:
            self.log.info("Label encoding categorical features.. Started")
            # creating instance of LabelEncoder
            le = LabelEncoder()
            # encoding categorical features
            data[cat_col] = le.fit_transform(data[cat_col]) # replacing categorical features with encoded values.
            self.log.info("Label encoding categorical features... Completed")
            # storing label encoding with respective feature label
            # creating empty dictionary to store label encoding
            label_encoding_dict = dict() # creating an empty dictionary
            for num, label in enumerate(le.classes_):
                label_encoding_dict[label] = num # storing label encoding with respective feature label
            self.log.info("Label encoding categorical features.. Stored")
            #as we need to jsonify it later so we return data and the dictionary
            return data, label_encoding_dict # return data after encoding categorical features and label encoding dictionary


        except Exception as e:
            self.log.error("Error occured while label encoding categorical features " + str(e))
            raise Exception("Error occured while label encoding categorical features " + str(e))