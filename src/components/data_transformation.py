import sys
import os
from dataclasses import dataclass
import pandas as pd
import numpy as np
from src.logger import logging
from src.exception import CustomException
from src.utils import save_object

from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler

@dataclass
class DataTransformationConfig:
    preprocessor_obj_file_path: str= os.path.join("artifact", "preprocessor.pkl")

class DataTransformation:
    def __init__(self):
        self.data_transformation_config = DataTransformationConfig()
    
    def get_data_transformer_obj(self):

        '''
        This function is used for the data transformation of the dataset.
        '''

        try:
            input_features = ['bedrooms', 'bathrooms', 'sqft_living', 'sqft_lot', 'floors', 'waterfront', 'view', 'condition',
                             'grade', 'sqft_above', 'sqft_basement', 'yr_built', 'yr_renovated', 'lat', 'long',
                            'sqft_living15', 'sqft_lot15', 'year','month','house_age']

            # Pipeline for handling missing values and scaling the data
            input_pipline = Pipeline(
                steps=[
                    ('imputer', SimpleImputer(strategy='median')),     # Handle missing values
                    ('scaler', StandardScaler())                       # Scaling the data
                ]
            )

            logging.info(f"Independent features: {input_features}")
            logging.info("Preprocessing pipeline created successfully")

            # Preprocessing for independent features data
            preprocessor = ColumnTransformer(
                [
                    ('input_pipeline', input_pipline, input_features)
                ]
            )

            return preprocessor
                
        except CustomException as e:
            raise CustomException(e,sys)
        
    def initiate_data_transformation(self,train_path,test_path):
        try:
            train_df = pd.read_csv(train_path)
            test_df = pd.read_csv(test_path)
            logging.info("Reading the train and test dataset is completed")

            logging.info("Obtaining the preprocessor object")
            preprocessing_obj = self.get_data_transformer_obj()

            target_col_name = 'price'

            input_feature_train_df = train_df.drop(target_col_name, axis=1)
            target_feature_train_df = train_df[target_col_name]

            input_feature_test_df = test_df.drop(target_col_name, axis=1)
            target_feature_test_df = test_df[target_col_name]

            logging.info('Applying preprocessing object on training and testing dataframe')

            input_feature_train_arr = preprocessing_obj.fit_transform(input_feature_train_df)
            input_feature_test_arr = preprocessing_obj.transform(input_feature_test_df)

            train_arr = np.c_[input_feature_train_arr, np.array(target_feature_train_df)]
            test_arr = np.c_[input_feature_test_arr, np.array(target_feature_test_df)]

            logging.info("Data transformation is successfully completed")

            save_object(
                file_path=self.data_transformation_config.preprocessor_obj_file_path,
                obj = preprocessing_obj
            )
            logging.info("Preprocessor object saved successfully")

            return(
                train_arr,
                test_arr,
                self.data_transformation_config.preprocessor_obj_file_path
            )
        
        except CustomException as e:
            raise CustomException(e,sys)
