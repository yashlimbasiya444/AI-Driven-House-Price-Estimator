import streamlit as st
import pandas as pd
import numpy as np
import pickle

# Load the model
model = pickle.load(open('model.pkl', 'rb'))

# Load the DataFrame if needed
df = pickle.load(open('df.pkl', 'rb'))

# Set the background color and title
st.markdown(
    """
    <style>
    .reportview-container {
        background: linear-gradient(to right, #f8f9fa, #e9ecef);
        padding: 20px;
    }
    .title {
        text-align: center;
        font-size: 40px;
        color: #007BFF;
        margin-bottom: 20px;
    }
    .subheader {
        text-align: center;
        font-size: 24px;
        color: #6c757d;
        margin-bottom: 40px;
    }
    .footer {
        text-align: center;
        font-size: 14px;
        color: #495057;
        margin-top: 20px;
    }
    .disclaimer {
        text-align: center;
        font-size: 16px;
        color: #dc3545;  /* Bootstrap danger color for emphasis */
        margin-bottom: 20px;
    }
    </style>
    """, unsafe_allow_html=True
)

# Streamlit app title
st.markdown('<h1 class="title">🏡 House Price Prediction App</h1>', unsafe_allow_html=True)
st.markdown('<h2 class="subheader">Get an estimated house price based on the features below</h2>', unsafe_allow_html=True)

# Add a disclaimer about the model's limitations
st.markdown(
    """
    <div class="disclaimer">
        ⚠️ <strong>Disclaimer:</strong> This model is for educational purposes and may not provide perfect predictions. 
        For best results, please enter values within the suggested ranges.
    </div>
    """, unsafe_allow_html=True
)

# Create two columns for a more organized layout
col1, col2 = st.columns(2)

with col1:
    st.markdown("##### 💰 Average Area Income")
    st.caption("Recommended range: $18,000 – $108,000")
    average_area_income = st.number_input(
        "Enter the average income in the area in dollars.",
        min_value=18000,
        max_value=108000,
        placeholder="e.g., 65000"
    )

    st.markdown("##### 🏠 Average Age of House")
    st.caption("Recommended range: 2 – 10 years")
    average_age_of_house = st.number_input(
        "Enter the average age of houses in the area in years.",
        min_value=2.0,
        max_value=10.0,
        step=0.1,
        format="%.1f",
        placeholder="e.g., 5.5"
    )

with col2:
    st.markdown("##### 🛏️ Number of Rooms")
    st.caption("Recommended range: 3 – 11")
    number_of_rooms = st.number_input(
        "Enter the average number of rooms in the houses.",
        min_value=3,
        max_value=11,
        placeholder="e.g., 7"
    )

    st.markdown("##### 🛌 Number of Bedrooms")
    st.caption("Recommended range: 2 – 7")
    number_of_bedrooms = st.number_input(
        "Enter the average number of bedrooms in the houses.",
        min_value=2,
        max_value=7,
        placeholder="e.g., 4"
    )
    
    st.markdown("##### 👥 Area Population")
    st.caption("Recommended range: 200 – 70,000")
    area_population = st.number_input(
        "Enter the total population in the area.",
        min_value=200,
        max_value=70000,
        placeholder="e.g., 35000"
    )

# Button to predict
if st.button("🔍 Predict"):
    if not all([average_area_income, average_age_of_house, number_of_rooms, number_of_bedrooms, area_population]):
        st.error("Please fill in all the fields before predicting.")
    else:
        # Prepare input data for prediction
        input_data = np.array([[average_area_income, average_age_of_house, 
                                 number_of_rooms, number_of_bedrooms, 
                                 area_population]])
        
        # Make prediction
        prediction = model.predict(input_data)
        
        # Display prediction result
        st.subheader("✨ Prediction Result")
        st.write(f"The predicted price for the house is: **${prediction[0]:,.2f}**")

# Add a footer
st.markdown(
    """
    <div class="footer">
        Developed for the House Price Prediction Project
    </div>
    """, unsafe_allow_html=True
)