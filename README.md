# 🚗 Car Price Prediction App

This repository contains a Streamlit-based web application that predicts the price of used cars based on various features like car model, location, year of manufacture, and more. The prediction is performed using a pre-trained Linear Regression model saved in a pickle file.

## 📋 Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Data](#data)
- [Model Training](#model-training)
- [Streamlit Application](#streamlit-application)
- [Future Enhancements](#future-enhancements)
- [Contributing](#contributing)
- [License](#license)

## 📝 Introduction

This application provides an easy-to-use interface for predicting the price of a used car. It leverages machine learning to estimate the value based on several input features such as the car's make, model, year, mileage, and other characteristics.

## ✨ Features

- **User-Friendly UI**: An interactive interface for inputting car details.
- **Accurate Predictions**: Utilizes a Linear Regression model trained on a comprehensive dataset.
- **Real-time Estimations**: Get instant predictions upon entering car details.
- **Predefined Categories**: Dropdowns and input fields are populated with predefined categories to ensure accurate predictions.

## 🛠️ Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/Chandan0034/Car-Prediction.git
    cd Car-Prediction
    ```

2. Create a virtual environment and activate it:

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the required packages:

    ```bash
    pip install -r requirements.txt
    ```

4. Place the `LinearRegressionModel.pkl` and `CleanedData.csv` files in the root directory.

## 🚀 Usage

1. Run the Streamlit app:

    ```bash
    streamlit run app.py
    ```

2. Open your web browser and go to `http://localhost:8501`.

3. Enter the required car details in the provided fields and click on the **Predict** button to get the estimated car price.

## 📊 Data

The data used for training the model includes various features such as:

- **Name**: The model of the car.
- **Location**: The city where the car is being sold.
- **Year**: The year of manufacture.
- **Kilometers Driven**: Total kilometers the car has been driven.
- **Fuel Type**: The type of fuel used by the car (Petrol, Diesel, CNG, etc.).
- **Transmission**: Type of transmission (Automatic or Manual).
- **Owner Type**: Number of previous owners (First, Second, etc.).
- **Mileage**: Fuel efficiency of the car.
- **Engine**: Engine capacity in CC.
- **Power**: The power output of the car in BHP.
- **Company Name**: The manufacturer of the car.

## 🤖 Model Training

The model used in this application is a Linear Regression model trained using scikit-learn. The training process involved the following steps:

1. **Data Preprocessing**: Handling categorical features with OneHotEncoding and normalizing numerical features.
2. **Model Training**: Using the `LinearRegression` class from scikit-learn to train the model on the cleaned dataset.
3. **Model Evaluation**: Evaluating the model using metrics like R-squared score to ensure accuracy.

## 🌐 Streamlit Application

The Streamlit app provides an easy-to-use interface for users to input car details and get instant price predictions. It includes the following features:

- **Input Form**: Fields for entering car details such as model, location, year, mileage, etc.
- **Predictions**: Displays the predicted price based on user input.
- **Interactive Design**: Enhanced UI/UX with clear section headings, tooltips, and custom styling.

## 🔮 Future Enhancements

- **Feature Addition**: Include more features like 'Seats', 'Color', etc., for a more comprehensive prediction.
- **Model Improvement**: Experiment with other machine learning models like Random Forest, Gradient Boosting, etc., for better accuracy.
- **Deployment**: Deploy the app on cloud platforms like Heroku, AWS, or GCP for wider accessibility.

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Commit your changes (`git commit -m 'Add some feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Open a pull request.

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
