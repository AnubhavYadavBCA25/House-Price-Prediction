import streamlit as st
import joblib
import pandas as pd
import numpy as np

import mysql.connector
from mysql.connector import Error

st.set_page_config(
    page_title="Prediction",
    page_icon="🔮",
)
st.sidebar.header("🔮Price Prediction")

def load_model(file_path):
    try:
        model = joblib.load(file_path)
        return model
    except Exception as e:
        st.error(f"Error loading model: {e}")
        return None
    
def load_scaler(file_path):
    try:
        scaler = joblib.load(file_path)
        return scaler
    except Exception as e:
        st.error(f"Error loading scaler: {e}")
        return None

def load_processed_data(file_path):
    try:
        data = pd.read_csv(file_path)
        return data
    except Exception as e:
        st.error(f"Error loading data: {e}")
        return None
    
# Load model, scaler, and processed data
model = load_model('artifacts/xgb_model.pkl')
scaler = load_scaler('artifacts/scaler.pkl')
data = load_processed_data('notebooks/data/processed_data.csv')

def predict_price(model, scaler, data, input_data):
    try:
        # Scale the input data
        input_data_scaled = scaler.transform(input_data)
        # Predict the price
        predicted_price = model.predict(input_data_scaled)
        return predicted_price
    except Exception as e:
        st.error(f"Error predicting price: {e}")
        return None

# Function to create a connection to the database
def create_connection():
    try:
        connection = mysql.connector.connect(
            host='localhost',
            port='3306',
            user='root',
            password='Anubhav@2023?',  # Replace with your MySQL root password
            database='house_price'
        )
        if connection.is_connected():
            st.success("Successfully connected to the database")
        return connection
    except Error as e:
        st.write(f"Error: '{e}'")
        return None
    
# Create house_price_prediction table in the database
def create_table(connection):
    try:
        cursor = connection.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS house_price_prediction (
                id INT AUTO_INCREMENT PRIMARY KEY,
                bedrooms INT,
                bathrooms FLOAT,
                sqft_living INT,
                sqft_lot INT,
                floors FLOAT,
                waterfront INT,
                view INT,
                `condition` INT,
                grade INT,
                sqft_above INT,
                sqft_basement INT,
                yr_built INT,
                yr_renovated INT,
                lat FLOAT,
                `long` FLOAT,
                sqft_living15 INT,
                sqft_lot15 INT,
                year INT,
                month INT,
                house_age INT,
                predicted_price FLOAT
            )
        ''')
    except Error as e:
        st.write(f"Error: '{e}'")

# Function to insert input data into the database
def insert_data(connection, bedrooms, bathrooms, sqft_living, sqft_lot, floors, waterfront, view, condition, grade, sqft_above, 
                sqft_basement, yr_built, yr_renovated, lat, long, sqft_living15, sqft_lot15, year, month, house_age, predicted_price):
    try:
        cursor = connection.cursor()
        predict_price = np.round(predicted_price[0], 2)
        cursor.execute(f"INSERT INTO house_price_prediction (bedrooms, bathrooms, sqft_living, sqft_lot, floors, waterfront, view, `condition`, grade, sqft_above, sqft_basement, yr_built, yr_renovated, lat, `long`, sqft_living15, sqft_lot15, year, month, house_age, predicted_price) VALUES ({bedrooms}, {bathrooms}, {sqft_living}, {sqft_lot}, {floors}, {waterfront}, {view}, {condition}, {grade}, {sqft_above}, {sqft_basement}, {yr_built}, {yr_renovated}, {lat}, {long}, {sqft_living15}, {sqft_lot15}, {year}, {month}, {house_age}, {predict_price})")
        connection.commit()
    except Error as e:
        st.write(f"Error: '{e}'")

def main():
    st.title('🔮 Price Prediction')
    st.subheader('Welcome to the Price Prediction Page!', divider='rainbow')

    st.header('Predict House Price 🏠')
    st.write('''In this section, you can input the features of a house and get the predicted price of the house.''')
    st.divider()
    
    # Input form fields
    st.write('Enter the number of bedrooms')
    bedrooms = st.slider('Bedrooms', min_value=1, max_value=10, value=3)
    st.divider()

    st.write('Enter the number of bathrooms')
    bathrooms = st.slider('Bathrooms', min_value=1.0, max_value=8.0, value=2.0, step=0.25)
    st.markdown('*Note: 0.5 indicates a bathroom with a toilet but no shower.*')
    st.divider()

    st.write('Enter the square feet of living area')
    sqft_living = st.number_input('Sqft Living', min_value=370, max_value=13540, value=1820)
    st.divider()

    st.write('Enter the square feet of lot area')
    sqft_lot = st.number_input('Sqft Lot', min_value=520, max_value=1651359, value=7242)
    st.divider()

    st.write('Enter the square feet of above ground living area')
    floors = st.slider('Floors', min_value=1.0, max_value=3.5, value=1.0, step=0.5)
    st.markdown('*Note: 1.0 indicates one floor. 0.5 indicates one floor with a basement.*')
    st.divider()

    st.write('Enter the waterfront view of the house')
    waterfront = st.selectbox('Waterfront', ['No', 'Yes'])
    if waterfront == 'Yes':
        waterfront = 1
    else:
        waterfront = 0
    st.divider()

    st.write('Enter the view of the house')
    view = st.slider('View', min_value=0, max_value=4, value=0)
    st.markdown('*Note: 0 indicates no view. 4 indicates an excellent view.*')
    st.divider()

    st.write('Enter the condition of the house')
    condition = st.slider('Condition', min_value=1, max_value=5, value=3)
    st.markdown('*Note: 1 indicates poor condition. 5 indicates excellent condition.*')
    st.divider()

    st.write('Enter the grade of the house')
    grade = st.slider('Grade', min_value=1, max_value=13, value=7)
    st.markdown('*Note: Represents the construction quality of improvements.*')
    st.divider()

    st.write('Enter the above ground square feet of the house')
    sqft_above = st.number_input('Sqft Above', min_value=370, max_value=9410, value=1660)
    st.markdown('*Note: Does not include basement area.*')
    st.divider()

    st.write('Enter the basement square feet of the house')
    sqft_basement = st.number_input('Sqft Basement', min_value=0, max_value=4820, value=160)
    st.markdown('*Note: 0 indicates no basement.*')
    st.divider()

    st.write('Enter the year the house was built')
    yr_built = st.number_input('Year Built', min_value=1900, max_value=2015, value=1950)
    st.divider()

    st.write('Enter the year the house was renovated')
    yr_renovated = st.number_input('Year Renovated', min_value=0, max_value=2015, value=0)
    st.markdown("*Note: 0 indicates no renovation. Enter 0 if you don't have any idea about house renovation.*")
    st.divider()

    st.write('Enter the latitude of the house')
    lat = st.number_input('Latitude', min_value=47.1559, max_value=47.7776, value=47.5112)
    st.divider()

    st.write('Enter the longitude of the house')
    long = st.number_input('Longitude', min_value=-122.518, max_value=-121.315, value=-122.257)
    st.divider()

    st.write('Enter the living space area (in square feet) of the nearest 15 neighbors.')
    sqft_living_15 = st.number_input('Sqft Living of Nearest 15 Neighbors', min_value=390, max_value=6210, value=1820)
    st.divider()

    st.write('Enter the lot space area (in square feet) of the nearest 15 neighbors.')
    sqft_lot_15 = st.number_input('Sqft Lot of Nearest 15 Neighbors', min_value=650, max_value=871200, value=7620)
    st.divider()

    st.write('Enter the year when you buy the house')
    yr_sold = st.number_input('Year Sold', min_value=2014, max_value=2015, value=2014)
    st.divider()

    st.write('Enter the month when you buy the house')
    month_sold = st.slider('Month Sold', min_value=1, max_value=12, value=1)
    st.divider()

    st.write('Age of the house when sold')
    age = yr_sold - yr_built
    st.write(f'The age of the house when sold is {age} years. Enter it below.')
    house_age = st.number_input('House Age', min_value=0, max_value=115, value=age)

    # Create a dictionary of input data
    input_data = {
        'bedrooms': bedrooms,
        'bathrooms': bathrooms,
        'sqft_living': sqft_living,
        'sqft_lot': sqft_lot,
        'floors': floors,
        'waterfront': waterfront,
        'view': view,
        'condition': condition,
        'grade': grade,
        'sqft_above': sqft_above,
        'sqft_basement': sqft_basement,
        'yr_built': yr_built,
        'yr_renovated': yr_renovated,
        'lat': lat,
        'long': long,
        'sqft_living15': sqft_living_15,
        'sqft_lot15': sqft_lot_15,
        'year': yr_sold,
        'month': month_sold,
        'house_age': house_age
    }

    # Convert the input data to a into a DataFrame
    input_df = pd.DataFrame([input_data])

    # Predict the price
    if st.button('Predict Price'):
        predicted_price = predict_price(model, scaler, data, input_df)
        if predicted_price:
            st.success(f'The predicted price of the house is ${np.round(predicted_price[0], 2)}')
        else:
            st.error('Error predicting price')

    # # Connect to the database and insert the input and prediction
        connection = create_connection()
        if connection:
            insert_data(connection, bedrooms, bathrooms, sqft_living, sqft_lot, floors, waterfront, view, condition, grade, sqft_above,
                        sqft_basement, yr_built, yr_renovated, lat, long, sqft_living_15, sqft_lot_15, yr_sold, month_sold, house_age, predicted_price)
            connection.close()
            st.success("Data inserted successfully in database.")
        else:
            st.error("Error connecting to the database.")

    st.divider()

    # Note
    st.subheader('⚠️Please Note:')
    st.write('''
            - The predicted price is an estimate and may vary from the actual price.
            - The model is trained on the King County House Sales dataset and may not be accurate for other datasets.
            - The prediction is based on the features you provide. Please ensure the input data is accurate.
            - The predicted price is in USD ($).
            - The prediction is for educational purposes only.
            - The prediction is not financial advice.
            - The prediction is not a substitute for professional advice.
            - The prediction is not guaranteed.
            - The prediction is not a warranty or guarantee of the future price.
            - For any queries or issues, please contact the developer.
            ''')

    # Footer
    st.markdown("---")
    st.markdown(
    """
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.4/css/all.min.css">
    <div style="text-align:center;">
        <p>Made with ❤️ by Anubhav Yadav</p>
        <p>Follow me on 
            <a href="https://linkedin.com/in/anubhav-yadav-srm" target="_blank"><i class="fab fa-linkedin"></i>LinkedIn</a> | 
            <a href="https://github.com/AnubhavYadavBCA25" target="_blank"><i class="fab fa-github"></i>GitHub</a>
        </p>
    </div>
    """, unsafe_allow_html=True
)
    

if __name__ == '__main__':
    main()