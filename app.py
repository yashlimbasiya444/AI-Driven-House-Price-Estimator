import streamlit as st
import pickle
import json
import numpy as np
import pandas as pd
import altair as alt
from data import create_usertable, add_userdata, login_user
import sqlite3 # Database dekhne ke liye import karein

# --- Global variables ---
__model = None
__data_columns = None
__locations = None
__cleaned_data = None

def load_artifacts():
    """
    Model aur data files ko load karne wala function.
    """
    global __model, __data_columns, __locations, __cleaned_data
    if __model and __data_columns and __cleaned_data is not None:
        return

    st.spinner("Application resources load ")
    try:
        with open('banglore_home_prices_model.pickle', 'rb') as f:
            __model = pickle.load(f)

        with open('columns.json', 'r') as f:
            data = json.load(f)
            __data_columns = data['columns']
            __locations = __data_columns[3:]
            
        __cleaned_data = pd.read_csv('cleaned_house_data.csv')
    
    except FileNotFoundError as e:
        st.error(f"file was missing {e}.")
        st.stop()

def predict_price(location, sqft, bath, bhk):
    """
    User ke input ke aadhar par ghar ki keemat predict karta hai.
    """
    try:
        loc_index = __data_columns.index(location.lower())
    except ValueError:
        loc_index = -1

    x = np.zeros(len(__data_columns))
    x[0], x[1], x[2] = sqft, bath, bhk
    if loc_index >= 0:
        x[loc_index] = 1

    return round(__model.predict([x])[0], 2)

def view_all_users():
    """
    Database se saare users ki jaankari nikalta hai.
    """
    conn = sqlite3.connect('user_data.db')
    df = pd.read_sql_query("SELECT id, username, password FROM users", conn) # Sirf ID, Username, aur Password dikhaye
    conn.close()
    return df

# =====================================================================
# --- APPLICATION PAGES ---
# =====================================================================

def home_page():
    st.title("🏡 Bangalore House Price Predictor")
    st.write("Aproximate home price.")

    col1, col2 = st.columns(2)
    with col1:
        location = st.selectbox("Location select", __locations)
        sqft = st.number_input("Total Square Feet", 300, 30000, 1200, 50)
    with col2:
        bhk = st.slider("Bedrooms (BHK)", 1, 10, 2)
        bath = st.slider("Bathrooms", 1, 10, 2)

    if st.button("Predict the price", type="primary", use_container_width=True):
        with st.spinner('calculating aproximate price...'):
            predicted_price = predict_price(location, sqft, bath, bhk)
            st.success(f"**Aproximate file: ₹ {predicted_price} Lakhs**")
            
            if __cleaned_data is not None:
                st.subheader("Price Comparison Chart")
                location_data = __cleaned_data[__cleaned_data['location'] == location]
                
                if not location_data.empty:
                    avg_prices_by_bhk = location_data.groupby('bhk')['price'].mean().reset_index()
                    avg_prices_by_bhk['Color'] = avg_prices_by_bhk['bhk'].apply(lambda x: 'Your Selection' if x == bhk else 'Average')
                    
                    chart = alt.Chart(avg_prices_by_bhk).mark_bar().encode(
                        x=alt.X('bhk:O', title='Number of Bedrooms (BHK)'),
                        y=alt.Y('price', title='Average Price (in Lakhs)'),
                        color=alt.Color('Color', scale={'domain': ['Average', 'Your Selection'], 'range': ['#4A90E2', '#D0021B']}),
                        tooltip=[alt.Tooltip('bhk', title='BHK'), alt.Tooltip('price', title='Avg. Price (Lakhs)', format='$.2f')]
                    ).properties(title=f"Average Property Prices in {location}")
                    
                    st.altair_chart(chart, use_container_width=True)
                    st.markdown(
                        f"The **<font color='#D0021B'>red bar</font>** highlights the average price for a **{bhk} BHK** property in **{location}**.",
                        unsafe_allow_html=True
                    )
                else:
                    st.info(f"No pricing data available to generate a chart for '{location}'.")

def dataset_page():
    st.title("📖 Bengaluru House Prices Dataset")
    st.write("Yeh woh saaf kiya hua dataset hai jisse model ko train kiya gaya hai.")
    if __cleaned_data is not None:
        st.dataframe(__cleaned_data)
        st.write(f"The dataset contains **{__cleaned_data.shape[0]} rows** and **{__cleaned_data.shape[1]} columns**.")
    else:
        st.warning("Dataset could not be loaded.")

def about_page():
    st.title("ℹ️ Project information")
    st.markdown("""
    This application is an end-to-end data science project that predicts house prices in Bangalore, India.

    ### How it Works
    1.  **Data Collection & Cleaning:** The project uses the "Bengaluru House Price Data" dataset from Kaggle, which is then cleaned by handling missing values and removing outliers.
    2.  **Model Training:** A Linear Regression model is trained on the cleaned data to learn the relationship between house features and their prices.
    3.  **Web Application:** This interactive web app is built with Streamlit. It loads the pre-trained model to make live predictions based on your input.

    ### Technologies Used
    - **Python, Pandas, NumPy:** For data manipulation.
    - **Scikit-learn:** For building the machine learning model.
    - **Streamlit:** To create this interactive web application.
    - **Altair:** For creating the data visualizations.
    """)

def admin_page():
    """
    Admin ke liye page jo saare registered users ko dikhata hai.
    """
    st.title("🔑 Admin Panel: User Details")
    st.write("Yeh table database mein maujood sabhi registered users ko dikhata hai.")
    user_data = view_all_users()
    st.dataframe(user_data)


# =====================================================================
# --- MAIN APP LOGIC AND ROUTING ---
# =====================================================================

def main():
    st.set_page_config(page_title="House Price Predictor", layout="wide")

    # --- Session State Initialization ---
    if 'logged_in' not in st.session_state:
        st.session_state['logged_in'] = False
        st.session_state['username'] = ''
        st.session_state['role'] = '' # 'user' ya 'admin'
    if 'page' not in st.session_state:
        st.session_state['page'] = 'Home'

    # --- Routing Logic ---
    if st.session_state['logged_in']:
        load_artifacts()

        st.sidebar.title(f"Swagat Hai, {st.session_state['username']}!")
        
        # --- Sidebar Navigation ---
        if st.sidebar.button("🏠 Home", use_container_width=True): st.session_state.page = "Home"
        if st.sidebar.button("📖 Data Set", use_container_width=True): st.session_state.page = "Data Set"
        if st.sidebar.button("ℹ️ About", use_container_width=True): st.session_state.page = "About"
        
        # --- ADMIN KE LIYE KHAS BUTTON ---
        if st.session_state['role'] == 'admin':
            if st.sidebar.button("🔑 Admin", use_container_width=True):
                st.session_state.page = "Admin"
        
        st.sidebar.markdown("---")
        
        if st.sidebar.button("Logout", use_container_width=True):
            st.session_state['logged_in'] = False
            st.session_state['username'] = ''
            st.session_state['role'] = '' # Role reset karein
            st.session_state['page'] = 'Home'
            st.rerun()

        # --- Page Display ---
        if st.session_state.page == "Home": home_page()
        elif st.session_state.page == "Data Set": dataset_page()
        elif st.session_state.page == "About": about_page()
        elif st.session_state.page == "Admin": admin_page()

    else:
        # --- LOGIN/SIGNUP VIEW ---
        st.title("House Price Predictor Mein Swagat Hai")
        # --- ERROR FIX: Added a unique key to the selectbox ---
        choice = st.sidebar.selectbox("Menu", ["Login", "Sign Up"], key="login_signup_choice")
        create_usertable()

        if choice == "Login":
            st.subheader("Login Section")
            username = st.text_input("Username")
            password = st.text_input("Password", type='password')
            if st.button("Login"):
                if login_user(username, password):
                    st.session_state['logged_in'] = True
                    st.session_state['username'] = username
                    
                    # --- YEH CHECK KAREGA KI USER ADMIN HAI YA NAHI ---
                    if username == 'admin' and password == 'admin123':
                        st.session_state['role'] = 'admin'
                    else:
                        st.session_state['role'] = 'user'
                    st.rerun()
                else:
                    st.warning("wrong username or password")

        elif choice == "Sign Up":
            st.subheader("create New Account")
            new_user = st.text_input("Username")
            new_password = st.text_input("Password", type='password')
            if st.button("Sign Up"):
                if add_userdata(new_user, new_password):
                    st.success("successfully account created! login with your credentials")
                else:
                    st.error("username allready exixts. Try different username.")

if __name__ == '__main__':
    main()

