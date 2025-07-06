import streamlit as st
import pandas as pd

st.title("Coffee Sales Dashboard")
st.file_uploader("Upload your sales data (CSV)", type=["csv"])
uploaded_file = st.file_uploader("Upload your sales data (CSV)", type=["csv"])
if uploaded_file is not None:
    data = pd.read_csv(uploaded_file)
    st.write("Data Preview:")
    st.dataframe(data.head())

    st.subheader("Sales Summary")
    total_sales = data['Sales'].sum()
    st.metric("Total Sales", f"${total_sales:,.2f}")

    st.subheader("Sales by Coffee Type")
    sales_by_type = data.groupby('Coffee Type')['Sales'].sum().reset_index()
    st.bar_chart(sales_by_type.set_index('Coffee Type'))

    st.subheader("Sales Over Time")
    data['Date'] = pd.to_datetime(data['Date'])
    sales_over_time = data.groupby('Date')['Sales'].sum().reset_index()
    st.line_chart(sales_over_time.set_index('Date'))


file  = st.file_uploader("UPload your csv file", type=["csv"])

if file:
    df = pd.read_csv(file)
    st.subheader("Data Preview")
    st.dataframe(df)

if file:
    st.subheader("Summary Stats")
    st.write(df.describe())

if file:
    cities = df["City"].unique()
    selected_city = st.selectbox("Filter by cities", cities)
    filtered_data = df[df["City"] == selected_city]
    st.dataframe(filtered_data)