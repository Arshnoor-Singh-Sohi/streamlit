import streamlit as st

st.title("Hello, Streamlit!")
st.subheader("This is a simple Streamlit app.")
st.text("Welcome to your fist interactive app")
st.write("Choose your fav variety of coffee")

coffee = st.selectbox("Coffee variety", ["Espresso", "Latte", "Cappuccino", "Americano"])

st.write(f"You choose {coffee}. Excelent choise")

st.success("App is running successfully!")