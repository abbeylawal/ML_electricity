import streamlit as st
import os


def show():
    st.title("Electricity Demand and Supply Forecasting App")
    st.write("""
    Welcome to the app that forecasts electricity demand and supply gaps using Generative AI.
    Explore  work  the predictions for Sub-Saharan Africa.
    """)
    st.image("./asserts/img/home.jpg")  # Optional: Add a relevant image
