<a id="readme-top"></a>

# Bangalore House Price Prediction 🏡

![Banner](https://github.com/user-attachments/assets/7e3be8b8-4d6c-45de-9962-5ba5865e2ebc)

## Overview

This is an end-to-end data science project that predicts house prices in Bangalore, India. It uses a **Linear Regression** model trained on real-world data from the `bengaluru_house_prices (1).csv` dataset.

The project is deployed as an interactive web application using **Streamlit**. It's not just a simple predictor; it also includes a complete **user authentication** system (Login & Sign Up) using a SQLite database, as well as a special **admin panel** to view registered users.

<br>

## 🚀 Application Preview

*(This is the space for your output. You can add a screenshot or GIF of your application here.)*

<p align="center">
  <img src="https" alt="App Preview">
</p>

<br>

## ✨ Key Features

* **📈 Real-time Price Prediction:** Get instant price estimates (in Lakhs) based on location, square feet, bathrooms, and BHK.
* **👤 User Authentication:** A secure Login and Sign Up system built from scratch (using `data.py` and `SQLite`).
* **🔑 Admin Panel:** A special admin login (`admin`/`admin123`) to view a list of all registered users in the database.
* **📊 Data Exploration:** An interactive "Dataset" page to view the final `cleaned_house_data.csv` used for training.

<br>

## 🛠️ Tech Stack: Libraries, Skills & Methods

This project combines skills from data science, machine learning, and web application development.

### Programming & Libraries

* **`Python`**: The core language for the entire project.
* **`Streamlit`**: Used to build and serve the interactive, multi-page web application (`app.py`).
* **`Scikit-learn`**: The main library for machine learning. Used for `LinearRegression`, `GridSearchCV`, and `train_test_split`.
* **`Pandas`**: Used for all data loading, cleaning, and manipulation (`bengaluru_house_prices (1).csv` -> `cleaned_house_data.csv`).
* **`NumPy`**: Used for numerical operations and data transformations.
* **`SQLite`**: The database used to store user information (`user_data.db`) via the helper functions in `data.py`.
* **`Jupyter Notebook`**: Used for all data science experimentation, from cleaning to modeling (`house_price.ipynb`).
* **`Pickle`**: Used to save the trained machine learning model (`banglore_home_prices_model.pickle`).
* **`JSON`**: Used to save the list of data columns (`columns.json`).

### Data Science & ML Methods

* **Data Cleaning:** Handled messy real-world data, such as converting `size` (e.g., "2 BHK") into a numeric `bhk` column and averaging `total_sqft` values given as a range (e.g., "1000 - 1500").
* **Outlier Removal:** Applied domain knowledge (e.g., price-per-square-foot, bathrooms-to-BHK ratio) to identify and remove extreme outliers.
* **Feature Engineering:** Used **One-Hot Encoding** to convert the categorical `location` column into numerical features for the model.
* **Model Selection:** Used `GridSearchCV` to test and compare different regression models, ultimately selecting `LinearRegression` as the best performer.
* **Model Persistence:** Saved the final trained model (`.pickle`) and column list (`.json`) so the Streamlit app can load and use them for predictions.

<br>

## 🏁 How to Run

To run this project on your local machine, follow these steps:

1.  **Clone the repository:**
    ```bash
    git clone [your-repo-url]
    cd [your-project-directory]
    ```

2.  **Install the required libraries:**
    ```bash
    pip install streamlit pandas numpy scikit-learn altair
    ```

3.  **Run the Streamlit application:**
    ```bash
    streamlit run app.py
    ```

4.  Open your web browser and go to the local URL (usually `http://localhost:8501`).

<br>

## 🤝 Contributing

Contributions are welcome! If you have ideas for improvements or find any bugs, feel free to open an issue or fork the repository and submit a pull request.

<br>

## 📬 Get in Touch!

Feel free to reach out for collaborations or questions:

* [![GitHub](https://img.shields.io/badge/Github-yashlimbasiya444-blue?logo=github)](https://github.com/yashlimbasiya444) 💻 - Explore more projects by Yash Limbasiya.
* [![LinkedIn](https://img.shields.io/badge/LinkedIn-Yash%20Limbasiya-blue?logo=linkedin)](https://www.linkedin.com/in/yash-limbasiya-177268359) 🌐 - Let's connect professionally.
