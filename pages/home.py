import streamlit as st
import os


# def show():
#     try:
#         # Get the absolute path of the current file
#         current_dir = os.path.dirname(os.path.abspath(__file__))
#
#         # Construct the path to the image file
#         image_path = os.path.join(current_dir, 'asserts', 'img', 'home.jpg')
#         print(image_path)
#         # Check if the file exists
#         if not os.path.isfile(image_path):
#             st.error(f"Image file not found: {image_path}")
#             return
#
#         # Use the image in Streamlit
#         st.image(image_path)
#
#     except Exception as e:
#         st.error(f"Error loading image: {e}")

def show():
    st.title("Electricity Demand and Supply Forecasting App")
    st.write("""
    Welcome to the app that forecasts electricity demand and supply gaps using Generative AI.
    Explore  work  the predictions for Sub-Saharan Africa.
    """)
    st.image("./asserts/img/home.jpg")  # Optional: Add a relevant image
