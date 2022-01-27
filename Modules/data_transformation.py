# from Modules.setup_logger import setup_logger
# from Modules.data_loader import DataGetter
from setup_logger import setup_logger

print("data_transformation")


class DataTransformation:
    """
    Class for transforming data

    Methods covered in this :

    1. rename_columns
    2. remove_questionmark
    3. remove_for_one
    4. remove_unnecessary_space
    5. remove_comma
    6. str_to_float
    7. remove_K
    8. remove_hyphen
    9. split_at_dot
    10. add_000

    """

    def __init__(self):
        self.log = setup_logger("Datatransformation.log", 'logs/data_transformation.log')  # set up logger

    def rename_columns(self, data):
        """
        Method for renaming columns
        Description: It will change the column names to the required names

        Input : param : columns list : dataframe, old_columns_list: list, new_columns_list: list
        Output : return: dataframe after renaming the columns names

        On Failure: Raise ValueError, log error in application logger
        """
        try:
            self.log.info('Renaming columns Started')
            data = data.rename(columns={'name': 'Name', 'price': 'Price', 'cuisine': 'Cuisine', 'reviews': 'Ratings',
                                        'location': 'Location', 'no. of reviews': 'No. of Reviews'})
            self.log.info('Renaming columns Completed')
            return data  # returning the dataframe after renaming the columns

        except Exception as e:
            self.log.error("Error While Renaming the columns name " + str(e))
            raise e

    def remove_questionmark(self, data, col):
        """
        Method : remove_questionmark
        Description: Custom method for remove the ? from  columns

        Input: data : pandas dataframe
               col : column name
        Output: data : pandas dataframe

        On Failure: Raise ValueError, log error in application logger

        """
        try:
            self.log.info('Removing question mark started')
            if data[col].dtype != 'object':
                data[col] = data[col].astype(str)  # converting the column to string
            data[col] = data[col].str.replace('?', '')  # removing the comma from the values
            self.log.info('removing question mark from column Completed')
            return data  # returning the dataframe after removing the question mark

        except Exception as e:
            self.logger.error("Error While removing question mark from columns " + str(e))
            raise e

    def remove_for_one(self, data, col):
        """
                Method : remove_for_one
                Description: Custom method for removing "for one"

                Input: data : pandas dataframe
                       col : column name
                Output: data : pandas dataframe

                On Failure: Raise ValueError, log error in application logger

                """
        try:
            self.log.info('Removing for one from column Started')
            if data[col].dtype != 'object':
                data[col] = data[col].astype(str)  # converting the column to string
            data[col] = data[col].str.replace(' for one', '')  # removing the comma from the values
            self.log.info('Removing for one from column Completed')
            return data  # returning the dataframe after removing the comma from the values

        except Exception as e:
            self.logger.error("Error While removing ' for one' from columns " + str(e))
            raise e

    def remove_unnecessary_space(self, data, col):
        """
        method: remove_unnecessary_space
        Description: Custom methode for removing unnecessary space

        Input: data: pandas dataframe
        Output: data: pandas dataframe

        On Failure: Raise ValueError, log error in application logger
        """
        try:
            self.log.info('Removing unnecessary space from values Started')
            data[col] = data[col].astype(str)  # converting the column to string
            data[col] = data[col].str.replace(' ', '')  # removing the slash from the values

            self.log.info('Removing unnecessary space from values Completed')
            return data  # returning the dataframe after removing the slash from the values

        except Exception as e:
            self.log.error("Error While removing unecessary space from columns " + str(e))
            raise e

    def remove_comma(self, data, col):
        """
        Method: remove_comma
        Description: Custom method for removing "," or comma form values

        Input: data: pandas dataframe
                  col: column name that needs to be cleaned
        Output: data: pandas dataframe

        On Failure: Raise ValueError, log error in application logger
        """
        try:
            self.log.info('Removing comma from values Started')
            if data[col].dtype != 'object':
                data[col] = data[col].astype(str)  # converting the column to string
            data[col] = data[col].str.replace(',', '')  # removing the comma from the values

            self.log.info('Removing comma from values Completed')
            return data  # returning the dataframe after removing the comma from the values

        except Exception as e:
            self.logger.error("Error While removing comma from columns " + str(e))
            raise e

    def remove_hyphen(self, data, col):
        """
        Method: remove_hyphen
        Description: Custom method for removing "," or comma form values

        Input: data: pandas dataframe
                  col: column name that needs to be cleaned
        Output: data: pandas dataframe

        On Failure: Raise ValueError, log error in application logger
        """
        try:
            self.log.info('Removing hyphen from values Started')
            if data[col].dtype != 'object':
                data[col] = data[col].astype(str)  # converting the column to string
            data[col] = data[col].str.replace('-', '0')  # removing the hyphen from the values

            self.log.info('Removing hyphen from values Completed')
            return data  # returning the dataframe after removing the comma from the values

        except Exception as e:
            self.logger.error("Error While removing hyphen from columns " + str(e))
            raise e

    def str_to_float(self, data, col):
        """
        method: str_to_float
        Description: Custom method for transforming string to float value
        Input: data: pandas dataframe
        Output: data: pandas dataframe

        On Failure: Raise ValueError, log error in application logger
        """
        try:
            self.log.info('String to float values Started')

            data[col] = data[col].astype(float)  # converting the column to float  in that columns where we require

            self.log.info('String to float values Completed')
            return data  # returning the dataframe after removing the slash from the values

        except Exception as e:
            self.log.error("Error While transforming String to float values " + str(e))
            raise e

    def remove_K(self, data, col):
        """
        method: remove_K
        Description: Custom methode for removing "K" when the reviews are greater than 9999

        Input: data: pandas dataframe
        Output: data: pandas dataframe

        On Failure: Raise ValueError, log error in application logger
        """
        try:
            self.log.info('Removing K from values Started')
            data[col] = data[col].astype(str)  # converting the column to string
            data[col] = data[col].str.replace('K', '')  # removing the slash from the values

            self.log.info('Removing K from values Completed')
            return data  # returning the dataframe after removing the slash from the values

        except Exception as e:
            self.log.error("Error While removing K from columns " + str(e))
            raise e

    def split_at_dot(self, data, col):
        """
        Method: remove_comma
        Description: Custom method for removing "," or comma form values

        Input: data: pandas dataframe
                  col: column name that needs to be cleaned
        Output: data: pandas dataframe

        On Failure: Raise ValueError, log error in application logger
        """
        try:
            self.log.info('Splitting at dot from values Started')
            if data[col].dtype != 'object':
                data[col] = data[col].astype(str)  # converting the column to string
            data[col] = data[col].str.split('.')[0] + '000'
            self.log.info('Splitting at do from values Completed')
            return data  # returning the dataframe after removing the comma from the values

        except Exception as e:
            self.logger.error("Error While Splitting at dot from columns " + str(e))
            raise e

    def add_000(self, data, col):
        """
        Method: add_000
        Description: Custom method for adding "000"  values

        Input: data: pandas dataframe
                  col: column name that needs to be cleaned
        Output: data: pandas dataframe

        On Failure: Raise ValueError, log error in application logger
        """
        try:
            self.log.info('Adding 000 from values Started')
            if data[col].dtype != 'object':
                data[col] = data[col].astype(str)  # converting the column to string
            data[col] = data[col].replace('K', "").split(".")[0]

            self.log.info('Adding 000 from values Completed')
            return data  # returning the dataframe after removing the comma from the values

        except Exception as e:
            self.logger.error("Error While Adding 000 from columns " + str(e))
            raise e

    def make_target(self, data, target_col):
        """
        Method: make_target

        Input: data: (pandas dataframe)
            : target_col (str)

        Output: data: (pandas dataframe)
        On Failure: Raise Error, log error in application logger
        """
        try:
            self.log.info('Cleaning Target Columns')
            data[target_col] = data[target_col].astype(str)  # converting the column to string
            data = data.loc[data[target_col] != 'NEW']  # removing the rows with NEW]]
            data = data.loc[data[target_col] != "-"]  # removing the "-" from column

            # removing "/5" from rate columns
            data[target_col] = data[target_col].str.replace('/5', '')
            self.log.info("/5 remove from rate column")

            # making target columns as float type
            data[target_col] = data[target_col].astype(float)  # converting the column to float
            self.log.info('Cleaning Target Columns Completed')

            return data  # returning the dataframe after cleaning the target column
        except Exception as e:
            self.log.error("Error While making target " + str(e))
            raise e
