import pandas as pd  # pip install pandas openpyxl
import streamlit as st  # pip install streamlit


st.set_page_config(
    page_title = "Multipage App",
    page_icon = "🎇"
)

st.title("Main Page")
st.sidebar.success("Select a page above.")

# py -m streamlit run Homepage.py
