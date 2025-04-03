import streamlit as st
import pandas as pd

# Title and description
st.title("📈 Blackstone Stock Performance")
st.write(
    """
    Blackstone Inc. (BX) is one of the world's leading investment firms. 
    This app visualizes the (totally real) stock price increase over the past 10 years.
    """
)

# Simulated stock data for the past 10 years
# In a real-world scenario, you'd fetch this data from an API or a database
data = {
    "Year": [2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022],
    "Stock Price (USD)": [20, 25, 30, 35, 40, 45, 50, 55, 100, 90],
}

# Convert data to a DataFrame
df = pd.DataFrame(data)

# Display the data
st.subheader("📊 Stock Price Data")
st.write(df)

# Line chart for stock price trend
st.subheader("📈 Stock Price Trend")
st.line_chart(df.set_index("Year"))

# Additional insights
st.subheader("📌 Insights")
st.write(
    """
    - Blackstone's stock price has grown significantly over the past decade.
    - The stock price doubled between 2020 and 2021, reflecting strong performance.
    - Despite a slight dip in 2022, the overall trend remains upward.
    """
)

# Footer
st.write(
    "For more information about Blackstone, visit [blackstone.com](https://www.blackstone.com/)."
)
