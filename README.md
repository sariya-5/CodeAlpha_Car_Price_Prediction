# 🚗 Car Price Prediction using Machine Learning

A Machine Learning project that predicts the selling price of used cars based on various features such as present price, kilometers driven, fuel type, transmission type, ownership, and car age.

This project was developed as part of the **CodeAlpha Machine Learning Internship**.

---

## 📌 Project Overview

The objective of this project is to build a regression model capable of predicting the selling price of a used car using historical car data.

The workflow includes:

- Data Collection
- Data Cleaning
- Exploratory Data Analysis (EDA)
- Feature Engineering
- Model Building
- Model Evaluation
- Model Deployment using Streamlit

---

## 📂 Project Structure

```
CodeAlpha_Car_Price_Prediction
│
├── Car_Price_Prediction.ipynb      # Jupyter Notebook
├── app.py                          # Streamlit Web App
├── model.pkl                       # Trained Machine Learning Model
├── car data.csv                    # Dataset
├── requirements.txt                # Required Python Libraries
├── README.md                       # Project Documentation
├── .gitignore
```

---

## 🛠️ Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- Streamlit
- Joblib
- Jupyter Notebook

---

## 📊 Dataset Features

The dataset contains the following features:

- Car Name
- Year
- Present Price
- Selling Price (Target)
- Driven Kilometers
- Fuel Type
- Selling Type
- Transmission
- Number of Previous Owners

---

## ⚙️ Machine Learning Workflow

### 1. Data Preprocessing

- Removed duplicate records
- Checked missing values
- Converted categorical variables into numerical values
- Created a new feature: **Car Age**

### 2. Exploratory Data Analysis

- Histogram
- Box Plot
- Scatter Plot
- Count Plot
- Correlation Heatmap
- Pair Plot

### 3. Model Building

Algorithm Used:

- Linear Regression

### 4. Model Evaluation

Evaluation Metrics:

- Mean Absolute Error (MAE)
- Mean Squared Error (MSE)
- Root Mean Squared Error (RMSE)
- R² Score

---

## ▶️ Installation

Clone the repository:

```bash
git clone https://github.com/sariya-5/CodeAlpha_Car_Price_Prediction.git
```

Go to the project directory:

```bash
cd CodeAlpha_Car_Price_Prediction
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate the virtual environment:

### Windows

```bash
.venv\Scripts\activate
```

Install the required libraries:

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the Application

Run the Streamlit app:

```bash
streamlit run app.py
```

The application will open in your browser.

---

## 📈 Future Improvements

- Random Forest Regression
- XGBoost Regression
- Hyperparameter Tuning
- Model Comparison
- Feature Importance Visualization
- Deploy using Render
- Responsive UI Improvements

---

## 👩‍💻 Author

**Sariya Khan**

GitHub:
https://github.com/sariya-5

---

## ⭐ If you found this project useful

Please consider giving this repository a ⭐ on GitHub.
