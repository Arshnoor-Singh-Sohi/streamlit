import streamlit as st

st.title("Coffee Taste Poll")

col1, col2 = st.columns(2)

with col1:
    st.header("Masala Coffee")
    vote1 = st.button("Vote for Masala Coffee")

with col2:
    st.header("Adrak Coffee")
    st.image("https://images.unsplash.com/photo-1603052875880-2f8b1c4d3a5e?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=800&q=60", use_column_width=True)
    vote1 = st.button("Vote for Adrak Coffee")

if vote1:
    st.success("Thank you for voting Masala Coffee!")
elif vote2:
    st.success("Thank you for voting Adrak Coffee!")

name = st.sidebar("Enter your name", placeholder="Your name here")
tea = st.sidebar.selectbox("Choose your tea type", ["Black", "Green", "Herbal"])

st.write(f"Hello, {name}! You chose {tea} tea. Enjoy your drink!")

with st.expander("Show Coffee Making Instructions"):
        st.write("""
    1. Boil water in a kettle.
    2. Add coffee grounds to a filter.
    3. Pour hot water over the coffee grounds.
    4. Let it brew for a few minutes.
    5. Pour the brewed coffee into a cup.
    6. Add sugar or milk as desired.
    7. Stir well and enjoy your coffee!
    """)

st.markdown('### Welcome to Coffee App')
st.markdown('> Blockquote: Enjoy your coffee with a smile!')

