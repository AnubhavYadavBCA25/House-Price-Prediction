import streamlit as st

st.set_page_config(
    page_title="Home",
    page_icon="🏠",
)
# Project introduction page of our house prediction project web app

def main():
    st.title('🏠House Price Prediction')
    st.subheader('Welcome to our House Price Prediction Project!')
    st.divider()

    st.header('Introduction 📚')
    st.write('''The real estate market is one of the most important sectors of the economy. The price of a house is influenced by 
             many factors such as location, size, number of bedrooms, number of bathrooms, etc. Predicting the price of a house is 
             a challenging task due to the complexity of the real estate market. In this project, we will use machine learning 
             algorithms to predict the price of a house based on its features.''')
    st.write('''The dataset used for this project is the King Country Housing dataset, which is a dataset that contains information 
             collected by the U.S Census Service concerning housing in the area of King County, Washington.''')
    st.write('''The dataset contains 21613 observations and 21 columns.''')
    st.write("Link to the dataset: [House Sales in King County, USA](https://www.kaggle.com/harlfoxem/housesalesprediction)")
    st.divider()

    st.header('Objective 🎯')
    st.write('''The main objective of this project is to predict the price of a house based on its features.''')
    st.divider()

    st.header('How It Works 🛠️')
    st.write("""
    1. Data Collection: The first step is to collect the data. We will use the Boston Housing dataset for this project.
    2. Data Preprocessing: The next step is to preprocess the data. We will clean the data, handle missing values, and encode categorical variables.
    3. Exploratory Data Analysis: We will perform exploratory data analysis to understand the data and identify patterns.
    4. Feature Engineering: We will create new features from the existing features to improve the performance of the model.
    5. Model Building: We will build a machine learning model to predict the price of a house.
    6. Model Evaluation: We will evaluate the performance of the model using various metrics.
    7. Selection of the Best Model: We will select the best model based on the evaluation metrics.
    8. Deployment: We will deploy the model as a web application using Streamlit.
    9. Prediction: Users can input the features of a house and get the predicted price of the house.
    10. Data Storage: We will store the data in a database for future use.
    11. Feedback: Users can provide feedback on the predictions.
""")
    st.divider()

    st.header('Technologies Used 🛠️')
    st.write("""
    1. Python: Python is a high-level, interpreted, and general-purpose programming language.
    2. Streamlit: Streamlit is an open-source app framework for Machine Learning and Data Science projects.
    3. Pandas: Pandas is a fast, powerful, flexible, and easy-to-use open-source data analysis and data manipulation library built on top of the Python programming language.
    4. NumPy: NumPy is a powerful open-source library for numerical computing in Python.
    5. Scikit-learn: Scikit-learn is a free machine learning library for Python.
    6. Matplotlib: Matplotlib is a comprehensive library for creating static, animated, and interactive visualizations in Python.
    7. Seaborn: Seaborn is a Python data visualization library based on Matplotlib.
    8. Plotly: Plotly is a graphing library for making interactive, publication-quality graphs online.        
    9. MySQL: MySQL is an open-source relational database management system.
""")
    st.divider()

    st.header('Explore Web App 🌐')
    st.write('Click on the sidebar to explore the different pages of the web app.')
    st.write('Or click on the link below to go to the home page of the web app.')
    st.write('[Predict House Price]()')
    st.divider()

    st.header('About Me👨‍💻')
    st.write('This project is developed by:')
    st.write("""
    Author: Anubhav Yadav

    Contact: anubhavyadav77ff@gmail.com

    GitHub: AnubhavYadavBCA25 (https://github.com/AnubhavYadavBCA25)
             
    LinkedIn: Anubhav Yadav (https://www.linkedin.com/in/anubhav-yadav-srm/)
    """)

if __name__ == '__main__':
    main()
    