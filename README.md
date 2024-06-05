# 🏠 House Price Prediction Project

## General Structure of this Project
- Title: House Price Prediction
- Description: The "House Price Prediction Project" leverages machine learning techniques to predict the sale prices of houses in King County, USA. Utilizing the "House Sales in King County" dataset, which contains detailed information on home sales from May 2014 to May 2015, the project aims to develop an accurate model that can estimate house prices based on various features such as the number of bedrooms, bathrooms, square footage, and location.

## Content

### About the Dataset
- Source of Dataset: https://www.kaggle.com/datasets/harlfoxem/housesalesprediction
- Context: The "House Sales in King County, USA" dataset provides comprehensive information on home sales in King County, which includes Seattle, from May 2014 to May 2015. The dataset consists of 21,613 records, each containing various features that describe the properties, such as the number of bedrooms and bathrooms, square footage, lot size, year built, and geographic location. This dataset serves as a valuable resource for building predictive models to estimate house prices based on these features, offering insights into the factors that influence real estate values in the region.
- Key features include:
    - Date: Represents the date when the house sale was recorded.
    - Price: The sale price of the house.
    - Bedrooms: Number of bedrooms.
    - Bathrooms: Number of bathrooms.
    - Sqft_living: Square footage of the living space.
    - Sqft_lot: Square footage of the lot.
    - Floors: Number of floors in the house.
    - Waterfront: A binary variable indicating if the house has a waterfront view.
    - View: An index from 0 to 4 of how good the view of the property was.
    - Condition: An index from 1 to 5 on the condition of the house.
    - Grade: An index from 1 to 13, where 1-3 falls short of building construction and design, 7 has an average level of construction and design, and 11-13 have a high-quality level of construction and design.
    - Sqft_above: Square footage of the house apart from the basement.
    - Sqft_basement: Square footage of the basement.
    - Year_built: The year the house was originally built.
    - Year_renovated: The year the house was last renovated.
    - Zipcode: The ZIP code in which the house is located.
    - Latitude and Longitude: Geographical coordinates of the house.

## Project Goal

The goal of this project is to develop a machine learning model that accurately predicts house prices in King County, USA, based on various property features. By analyzing and leveraging the "House Sales in King County" dataset, the project aims to identify key factors influencing home values and provide a reliable tool for estimating market prices.

## Installation (IDE's, Libraries and etc)
1. IDE:
- VSCode : Data Analysis,Pipeline Building, Transformation, Data Ingestion, ML Modelling and Web App. Development (Prefered)
- PyCharm : Data Analysis,Pipeline Building, Transformation, Data Ingestion, ML Modelling and Web App. Development (Prefered)
- Jupyter Notebook : Analysis and ML Modelling.
- Google Colab : Analysis and ML Modelling.
- Python Virtual Enviornment v3.8 (Prefered)
2. Python Libraries:
- Pandas (Data Manipulation)
- Matplotlib and Seaborn (Data Visualization)
- Scikit-learn (Machine Learning Model)
- Streamlit (Web Application)
- Plotly (Interactive Visualization)
- XGBoost (ML Algorithm)
- OS (Directory Work)
- Joblib (Pickle file making and loading)

## Step-By-Step Project Overview

1. **Data Acquisition**: Download the "House Sales in King County" dataset from the provided source (https://www.kaggle.com/datasets/harlfoxem/housesalesprediction) and save it in a local directory.

2. **Data Exploration**: Load the dataset into a pandas DataFrame and perform initial exploratory data analysis (EDA) to gain insights into the data. This includes checking for missing values, data types, statistical summaries, and visualizations.

3. **Data Preprocessing**: Clean the data by handling missing values, outliers, and any inconsistencies in the dataset. This may involve imputing missing values, removing outliers, and transforming variables if necessary.

4. **Feature Engineering**: Create new features or transform existing features to enhance the predictive power of the model. This may include feature scaling, one-hot encoding categorical variables, and creating interaction or polynomial features.

5. **Feature Selection**: Select the most relevant features that have the strongest correlation with the target variable (house prices). This can be done using statistical tests, feature importance techniques, or domain knowledge.

6. **Model Development**: Split the dataset into training and testing sets. Train various machine learning models, such as linear regression, decision trees, random forests, or XGBoost, using the training data. Evaluate the performance of each model using appropriate evaluation metrics.

7. **Model Evaluation**: Compare the performance of different models based on evaluation metrics such as mean squared error (MSE), root mean squared error (RMSE), and R-squared. Select the best-performing model for further analysis.

8. **Model Fine-tuning**: Fine-tune the selected model by optimizing hyperparameters using techniques like grid search or random search. This helps to improve the model's performance and generalization ability. (Depend on Model Performance)

9. **Model Validation**: Validate the final model using the testing set to assess its performance on unseen data. Calculate evaluation metrics and analyze the model's predictions.

10. **Model Deployment**: Build a web application using Streamlit to create an interactive interface for users to input property features and get predicted house prices. Deploy the application on a web server or cloud platform for accessibility.

11. **Documentation and Reporting**: Document the entire project, including the steps taken, methodologies used, and results obtained. Create a comprehensive report summarizing the findings, insights, and recommendations.

By following these step-by-step procedures, you can successfully develop a machine learning model for house price prediction in King County, USA.

## Web Application (Streamlit)

Web App Link: 

## Contact Information
- LinkedIn: https://www.linkedin.com/in/anubhav-yadav-data-science/
- Email: anubhavyadav77ff@gmail.com