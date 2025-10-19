# 🏡 House Price Predictor

## Overview
**House Price Predictor** is an interactive web application built using **Streamlit** and **scikit-learn**.  
It predicts house prices based on several key factors like income, house age, number of rooms, bedrooms, and population in the area.

This project combines **machine learning** with a **simple and intuitive interface** — allowing users to enter details and instantly get a predicted house price.  
It also features a lightweight **user authentication system (login/signup)** built with **SQLite** for secure user access.

---

## 🎥 Live Demo
🚀 *Coming soon!*  

Try the app and explore how data and AI can predict property values. Just enter your housing details and get an instant estimate!

---

## 🗺️ Learning Journey

### Inspiration
The real estate market is full of uncertainty, and I wanted to create a simple data-driven tool to help visualize housing trends and understand price factors.

### Challenges Faced
- **Data Cleaning:** Ensuring the dataset was accurate and ready for training.  
- **Model Tuning:** Finding the right regression model with minimal error.  
- **Authentication:** Building a basic, secure login/signup system.  
- **Interface Design:** Keeping the Streamlit app minimal yet functional.

### What I Learned
- Hands-on experience with **data preprocessing**, **feature scaling**, and **regression modeling**.  
- Building **Streamlit** apps for real-world use.  
- Using **SQLite** for backend authentication.  
- Visualizing data to uncover feature importance and correlations.

---

## 📋 Table of Contents
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Technologies Used](#technologies-used)
- [Dataset](#dataset)
- [Model Training](#model-training)
- [Results](#results)
- [Directory Structure](#directory-structure)
- [Future Enhancements](#future-enhancements)
- [Contributing](#contributing)
- [Contact](#contact)

---

## 🌟 Features

- **Accurate Predictions:** Trained linear regression model for reliable results.  
- **Interactive UI:** User-friendly Streamlit web interface.  
- **User Authentication:** Login and signup system using SQLite.  
- **Data Visualization:** Jupyter Notebook includes exploratory data analysis and charts.  
- **Reusable Model:** Model saved as a `.pkl` file for easy deployment.

---

## 🛠 Installation

1. **Clone the Repository**
   ```bash
   git clone https://github.com/Yash-Limbasiya/House-Price-Predictor.git
   cd House-Price-Predictor
   ```

2. **Create and Activate Virtual Environment (optional)**
   ```bash
   python -m venv venv
   source venv/bin/activate       # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the App**
   ```bash
   streamlit run app.py
   ```

---

## 🚀 Usage

### Run the Streamlit App
```bash
streamlit run app.py
```
Enter the house parameters (income, age, rooms, etc.) to get an instant prediction.

### Explore Data & Model
Open the Jupyter Notebook to explore data insights and model training:
```bash
jupyter notebook house_price.ipynb
```

---

## 💻 Technologies Used
- **Python**
- **Streamlit**
- **scikit-learn**
- **Pandas**, **NumPy**, **Matplotlib**, **Seaborn**
- **SQLite3**
- **pickle**

---

## 📊 Dataset
**File:** `cleaned_house_data.csv`  
Contains features such as:
- Average Area Income  
- Average House Age  
- Average Number of Rooms  
- Average Number of Bedrooms  
- Area Population  
- House Price *(target variable)*  

---

## 🧠 Model Training
- Model used: **Linear Regression**
- Evaluation Metrics:
  - **R² Score:** `0.8017`
  - **Coefficients:** `[0.854, 0.835, 0.823, 0.844, 0.816]`
- Model saved as `model.pkl` for reuse in the app.

---

## 🏆 Results
The model achieves solid prediction accuracy, effectively learning relationships between housing features and price outcomes.

---

## 📁 Directory Structure
```
House-Price-Predictor/
├── app.py                     # Streamlit app
├── data.py                    # User authentication logic
├── cleaned_house_data.csv     # Dataset
├── house_price.ipynb          # Notebook for analysis and model training
├── model.pkl                  # Saved model
├── requirements.txt           # Project dependencies
└── README.md                  # Project documentation
```

---

## 🚀 Future Enhancements
- Add more regression models (Random Forest, XGBoost).  
- Improve the Streamlit UI with charts and interactive graphs.  
- Add “forgot password” functionality in the login system.  
- Integrate real-world APIs for live housing market data.  
- Make the app mobile-responsive.

---

## 🤝 Contributing
Contributions are welcome!  

1. **Fork** the repository.  
2. **Create a branch:**  
   ```bash
   git checkout -b feature/YourFeature
   ```
3. **Commit your changes:**  
   ```bash
   git commit -m "Add new feature"
   ```
4. **Push and open a Pull Request.**

Don’t forget to ⭐ the repo if you like it!

---

## 📬 Contact

**👨‍💻 Yash Limbasiya**  
- GitHub: [Yash-Limbasiya](https://github.com/Yash-Limbasiya)  
- LinkedIn: [Yash Limbasiya](https://linkedin.com/in/yash-limbasiya)  
- Email: [yash@example.com](mailto:yash@example.com)

> “A home is more than just a structure — it’s where dreams are built. Let data help you build your future.”
