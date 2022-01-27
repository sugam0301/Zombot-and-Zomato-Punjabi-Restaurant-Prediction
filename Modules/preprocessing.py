# from Modules.setup_logger import setup_logger
# from Modules.data_loader import DataGetter
# from Modules.preprocessor import Preprocessor
# from Modules.data_transformation import DataTransformation

from setup_logger import setup_logger
from data_loader import DataGetter
from preprocessor import Preprocessor
from data_transformation import DataTransformation


# creating custom class to process the data and saved it to local for feed to model.


class Preprocessing:
    """
    Write docstring here
    """

    def __init__(self):
        # create instance of logger
        self.df = df
        self.folder = './logs/'
        self.filename = 'preprocessing.txt'
        if not os.path.isdir(self.folder):
            os.mkdir(self.folder)
        self.log = setup_logger('preprocessing', self.folder + self.filename)
        self.data_loader = DataGetter()  # create instance of data loader
        self.preprocessor = Preprocessor()  # create instance of preprocessor
        # create instance of data transformation
        self.data_transformation = DataTransformation()

    def preprocess_data(self, data_path):
        """
        Method: preprocess_data.
        Description: This methode is for preprocessing the data.
        """
        try:
            self.log.info("Start preprocessing data")

            # Step 1
            # get the data from the data loader
            self.log.info("Loading data... Started")
            df = self.data_loader.data_getter(data_path)  # load data as dataframe
            print(df)
            self.log.info("Data loaded... Completed")

            # Step 2
            # renaming columns name
            self.log.info("Renaming Column name.. Started")

            df = self.data_transformation.rename_columns(data=df)
            self.log.info("Renaming Column name.. Completed")

            # Step 3
            # dropping the unwanted columns, came from EDA
            self.log.info("Dropping unwanted columns... Started")
            df = self.preprocessor.drop_columns(data=df, col_list=[
                'Location url',
                'Name',
            ])
            self.log.info("Unwanted columns dropped... Completed")

            # Step 4
            # dropping null values from the dataframe
            self.log.info("Dropping null values... Started")
            df = self.preprocessor.drop_null(data=df)
            print("hi")
            self.log.info("Null values dropped... Completed")

            # Step 5
            # dropping duplicate values from the dataframe
            self.log.info("Dropping duplicate values... Started")
            df = self.preprocessor.drop_duplicates(data=df)
            self.log.info("Duplicate values dropped... Completed")

            # steps 6 
            # remove question mark from price column
            self.log.info("remove question mark from column... Started")
            df = self.data_transformation.remove_questionmark(data=df, col="Price")
            self.log.info("remove question mark from column... Completed")

            # Step 7
            # remove for one from price
            self.log.info("remove for one from price... Started")
            df = self.data_transformation.remove_for_one(data=df, col="Price")
            self.log.info("remove for one from price... Completed")

            # Step 8
            # split at dot from No of reviews
            self.log.info("split at dot from No of reviews... Started")
            df = self.data_transformation.split_at_dot(data=df, col='No. of Reviews')
            self.log.info("split at dot from No of reviews... Completed")

            # Step 9
            # remove comma from No. of reviews
            self.log.info("split at dot from No of reviews... Started")
            df = self.data_transformation.remove_comma(data=df, col='No. of Reviews')
            self.log.info("split at dot from No of reviews... Completed")

            # step 10
            # remove hyphen from Ratings
            self.log.info("remove hyphen from Ratings... Started")
            df = self.data_transformation.remove_comma(data=df, col='No. of Reviews')
            self.log.info("remove hyphen from Ratings... Completed")

            # Step 11
            # str_to_float in reviews , ratings
            self.log.info("str_to_float in ratings and reviews and also the price... Started")
            df = self.data_transformation.str_to_float(data=df, col='No. of Reviews')
            df = self.data_transformation.str_to_float(data=df, col='Price')
            df = self.data_transformation.str_to_float(data=df, col='Ratings')
            self.log.info("str_to_float in ratings and reviews... Completed")

            # step 12
            # fillna in the Ratings and no. of reviews
            self.log.info("fillna... started")
            df = self.preprocessor.fill_na(data=df, col="Ratings")
            df = self.preprocessor.fill_na(data=df, col="No. of Reviews")
            self.log.info("fillna... ended")

            # Step 13
            # Encoding categorical columns
            self.log.info("Encoding categorical columns... Started")
            # Encoding "Cuisine"
            df, cuisine_dict = self.preprocessor.label_encoding(data=df, cat_col="Cuisine")
            # saving in json file
            self.data_loader.save_json(cuisine_dict, "./encoding_dict/cuisine.json")

            # Encoding "city"
            df, city_dict = self.preprocessor.label_encoding(data=df, cat_col="City")
            print(city_dict)
            with open("./encoding_dict/city.json", 'w+') as f:
                json.dump(city_dict, f, indent=4)  # dumping dictionary as json file
            # saving in json file
            # self.data_loader.save_json(city_dict, "./encoding_dict/city.json")

            # Encoding location
            df, location_dict = self.preprocessor.label_encoding(data=df, cat_col="Location")
            # saving in json file
            print("hello")
            self.data_loader.save_json(location_dict, "location.json")

            self.log.info("Encoding categorical columns... Completed")

            # Step 14
            # saving the dataframe as csv file for model feeding
            self.log.info("Saving dataframe as csv file... Started")
            # self.data_loader.data_saved(df, "./data/preprocessed_data.csv")
            self.log.info("Saving dataframe as csv file... Completed")
            return df  # return the dataframe

        except Exception as e:
            self.log.info("Error on Preprocessing data " + str(e))
