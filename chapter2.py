import streamlit as st

st.title("Coffee Maker App")

if st.button("Make Coffee"):
    st.write("Brewing your coffee...")
    st.balloons()
    st.success("Your coffee is ready! Enjoy!")

add_sugar = st.checkbox("Add sugar", value=True)

if add_sugar:
    st.write("Sugar added to your coffee!")

tea_type = st.radio("Choose your tea type", ["Black", "Green", "Herbal"])
st.write(f"You chose {tea_type} tea. Enjoy your drink!")
flavour = st.selectbox("Choose a flavour", ["Vanilla", "Chocolate", "Caramel"])
st.write(f"You chose {flavour} flavour. Enjoy your drink!")

sugar = st.slider("Sugar level", 0, 10, 5)
st.write(f"You selected {sugar} teaspoons of sugar.")

st.number_input("Enter the number of cups", min_value=1, max_value=10, value=1)
st.text_input("Enter your name", placeholder="Your name here")

name = st.text_input("Enter your name", placeholder="Your name here")
if name:
    st.write(f"Hello, {name}! Welcome to the Coffee Maker App!")

dob = st.date_input("Select your date of birth")
if dob:
    st.write(f"Your date of birth is {dob}. Thank you for sharing!")