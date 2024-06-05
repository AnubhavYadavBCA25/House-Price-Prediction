import pandas as pd
import streamlit as st
import plotly.express as px
import matplotlib.pyplot as plt

st.set_page_config(
    page_title="Visualization",
    page_icon="📊",
)
st.sidebar.header("Data Visualization")

def main():
    st.title('📊 Visualization')
    st.subheader('Welcome to the Visualization Page!', divider='rainbow')

    st.header('Data Exploration 📊')
    st.write('''In this section, we will explore the dataset to understand the distribution of the features and identify patterns in the data.''')
    
    def load_data(file_path):
        try:
            data = pd.read_csv(file_path)
            return data
        except Exception as e:
            st.error(f"Error loading data: {e}")
            return None

    # Load data (replace 'your_file.csv' with your actual file path)
    file_path = 'notebooks/data/kc_house_data.csv'
    df = load_data(file_path)
    df_display = df.copy()
    df_display['date'] = pd.to_datetime(df_display['date'])
    st.dataframe(df_display)
    st.divider()

    # Display the summary of the data
    st.header('Data Summary 📈')
    st.write(df.describe())
    st.divider()

    # Display the price distribution
    st.header('Price Distribution 📊')
    fig = px.histogram(df, x='price', title='Price Distribution')
    st.plotly_chart(fig)
    st.write('Conclusions: The price distribution is right-skewed, which means that most of the houses have a lower price.')
    st.divider()

    # Map of houses based on location
    st.header('Map of Houses 🗺️')
    st.write('The map below shows the location of the houses in the dataset.')
    fig = px.scatter_mapbox(df, lat='lat', lon='long', color='price', size='price', hover_name='price', zoom=9, title='Map of King County Houses')
    fig.update_layout(mapbox_style='open-street-map', autosize=False, width=800, height=700)
    st.plotly_chart(fig)
    st.write('Conclusions: The houses are located in the King County area of Washington. The price of the houses is represented by the color and size of the markers.')
    st.divider()

    # Display scatter plot of price vs sqft_living
    st.header('Price vs Sqft Living Scatter Plot 📈')
    fig = px.scatter(df, x='sqft_living', y='price', title='Price vs Sqft Living Scatter Plot', color='price', labels={'sqft_living': 'Sqft Living', 'price': 'Price'})
    st.plotly_chart(fig)
    st.write('Conclusions: The price of the house increases with the increase in the square feet of living area.')
    st.divider()

    # Display number of floors count plot
    st.header('Number of Floors Count Plot 📊')
    floor_counts = df['floors'].value_counts().reset_index()
    floor_counts.columns = ['floors', 'count']
    fig = px.bar(floor_counts, x='floors', y='count', title='Number of Floors Count Plot', labels={'floors': 'Floors', 'count': 'Count'}, color='floors')
    st.plotly_chart(fig)
    st.write('Conclusions: Most of the houses have 1 floor.')
    st.divider()

    # Display number of bedrooms count plot
    st.header('Number of Bedrooms Count Plot 📊')
    bedroom_counts = df['bedrooms'].value_counts().reset_index()
    bedroom_counts.columns = ['bedrooms', 'count']
    fig = px.bar(bedroom_counts, x='bedrooms', y='count', title='Number of Bedrooms Count Plot', labels={'bedrooms': 'Bedrooms', 'count': 'Count'}, color='bedrooms')
    st.plotly_chart(fig)
    st.write('Conclusions: Most of the houses have 3 bedrooms.')
    st.divider()

    # Display grade count plot
    st.header('Grade Count Plot 📊')
    grade_counts = df['grade'].value_counts().reset_index()
    grade_counts.columns = ['grade', 'count']
    fig = px.bar(grade_counts, x='grade', y='count', title='Grade Count Plot', labels={'grade': 'Grade', 'count': 'Count'}, color='grade')
    st.plotly_chart(fig)
    st.write('Conclusions: Most of the houses have a grade of 7, which is average.')
    st.divider()

    # Display condition count plot
    st.header('Condition Count Plot 📊')
    condition_counts = df['condition'].value_counts().reset_index()
    condition_counts.columns = ['condition', 'count']
    fig = px.bar(condition_counts, x='condition', y='count', title='Condition Count Plot', labels={'condition': 'Condition', 'count': 'Count'}, color='condition')
    st.plotly_chart(fig)
    st.write('Conclusions: Most of the houses have a condition of 3, which is average.')
    st.divider()

    # Display waterfront count plot
    st.header('Waterfront Count Plot 📊')
    waterfront_counts = df['waterfront'].value_counts().reset_index()
    waterfront_counts.columns = ['waterfront', 'count']
    fig = px.bar(waterfront_counts, x='waterfront', y='count', title='Waterfront Count Plot', labels={'waterfront': 'Waterfront', 'count': 'Count'}, color='waterfront')
    st.plotly_chart(fig)
    st.write('Conclusions: Most of the houses do not have a waterfront view.')
    st.divider()

    # Display view count plot
    st.header('View Count Plot 📊')
    view_counts = df['view'].value_counts().reset_index()
    view_counts.columns = ['view', 'count']
    fig = px.bar(view_counts, x='view', y='count', title='View Count Plot', labels={'view': 'View', 'count': 'Count'}, color='view')
    st.plotly_chart(fig)
    st.write('Conclusions: Most of the houses have a view of 0, which is average.')
    st.divider()

    # Display year built vs price line plot
    st.header('Year Built vs Price Line Plot 📈')
    year_price = df.groupby('yr_built')['price'].mean().reset_index()
    fig = px.line(year_price, x='yr_built', y='price', title='Year Built vs Price Line Plot', labels={'yr_built': 'Year Built', 'price': 'Price'})
    st.plotly_chart(fig)
    st.write('''Conclusions: The price of the houses increases with the year built. Newer houses tend to have a higher price. 
             Price of the houses decreases during the 2008 recession and 1940 due to the World War II.''')
    st.divider()

    # Display year renovated vs price line plot from 1934 to 2015
    st.header('Year Renovated vs Price Line Plot 📈')
    year_price = df.groupby('yr_renovated')['price'].mean().reset_index()
    year_price = year_price[year_price['yr_renovated'] != 0]
    year_price = year_price[(year_price['yr_renovated'] >= 1934) & (year_price['yr_renovated'] <= 2015)]
    fig = px.line(year_price, x='yr_renovated', y='price', title='Year Renovated vs Price Line Plot', labels={'yr_renovated': 'Year Renovated', 'price': 'Price'})
    st.plotly_chart(fig)
    st.write('Conclusions: The price of the houses increases with the year renovated.')
    st.divider()

    # Display date vs price line plot
    st.header('Date vs Price Line Plot 📈')
    date_price = df_display.groupby('date')['price'].mean().reset_index()
    fig = px.line(date_price, x='date', y='price', title='Date vs Price Line Plot', labels={'date': 'Date', 'price': 'Price'})
    st.plotly_chart(fig)
    st.write('Conclusions: The price of the houses increases with time.')
    st.divider()

    # Display month vs price line plot from January to December
    st.header('Month vs Price Line Plot 📈')
    df_display['month'] = df_display['date'].dt.month
    month_df = {'month': ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'],
                'price': df_display.groupby('month')['price'].mean().values}
    month_df = pd.DataFrame(month_df)
    fig = px.line(month_df, x='month', y='price', title='Month vs Price Line Plot', labels={'month': 'Month', 'price': 'Price'})
    st.plotly_chart(fig)
    st.write('Conclusions: The price of the houses is highest in May and June.')
    st.divider()

    # Conclusions
    st.header('Conclusions 📝')
    st.write('''
            - In this section, we explored the dataset to understand the distribution of the features and identify patterns in the data. 
            - We visualized the price distribution, map of houses, price vs sqft living scatter plot, number of floors count plot, number of bedrooms count plot, 
             grade count plot, condition count plot, waterfront count plot, view count plot, year built vs price line plot, year renovated vs price line plot, 
             date vs price line plot, and month vs price line plot. We made conclusions based on the visualizations.
            - We observed that the price of the houses increases with the increase in the square feet of living area.
            - Most of the houses have 1 floor, 3 bedrooms, and a grade of 7.
             - Most of the houses have a condition of 3, which is average.
             - Most of the houses do not have a waterfront view.
             - Most of the houses have a view of 0, which is average.
             - The price of the houses increases with the year built. Newer houses tend to have a higher price.
             - The price of the houses increases with the year renovated.
             - The price of the houses increases with time.
             - The price of the houses is highest in May and June. And lowest in January and February.
             - Check more visualization in our [GitHub Repository](https://github.com/AnubhavYadavBCA25/House-Price-Prediction/blob/main/notebooks/EDA.ipynb)''')



if __name__ == '__main__':
    main()
    
