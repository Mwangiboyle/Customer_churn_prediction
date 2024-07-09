## Customer Churn Prediction end to end project


![image](https://github.com/Mwangiboyle/Customer_churn_prediction/assets/92526613/ef6ba7cb-a991-4f53-8b4f-458eabb4499b)



## Introduction

Customer churn is a critical issue for businesses across various industries, particularly in the banking sector.
Churn refers to the phenomenon where customers stop doing business with a company over a specified period.
Understanding and predicting customer churn can help businesses implement strategies to retain customers, thus reducing loss and increasing profitability.

This project aims to build a machine learning model to predict customer churn for ABC Bank. By analyzing customer data, the model can identify patterns and indicators of churn, enabling the bank to take proactive measures to retain at-risk customers. Such predictions are crucial for improving customer satisfaction, optimizing marketing efforts, and enhancing overall business performance.

## Project Structure

- `data/`: Contains the dataset used for training and testing the model.
- `notebooks/`: Jupyter notebooks used for data exploration and model development.
- `scripts/`: Python scripts for data preprocessing, model training, and evaluation.
- `models/`: Directory where trained models are saved.
- `app/`: FastAPI application for deploying the model.
- `Dockerfile`: Dockerfile for containerizing the FastAPI application.
- `requirements.txt`: List of required Python packages.
- `README.md`: Project documentation.

## Dataset

The dataset contains the following columns:
- `customer_id`: Unique identifier for each customer.
- `credit_score`: Customer's credit score.
- `country`: Country of the customer.
- `gender`: Gender of the customer.
- `age`: Age of the customer.
- `tenure`: Number of years the customer has been with the bank.
- `balance`: Account balance of the customer.
- `products_number`: Number of products the customer is using.
- `credit_card`: Whether the customer has a credit card (1) or not (0).
- `active_member`: Whether the customer is an active member (1) or not (0).
- `estimated_salary`: Estimated salary of the customer.
- `churn`: Whether the customer has churned (1) or not (0).

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/customer-churn-prediction.git
    cd customer-churn-prediction
    ```

2. Create and activate a virtual environment:
    ```bash
    python -m venv venv
    source venv/bin/activate   # On Windows: venv\Scripts\activate
    ```

3. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

### Training the Model

1. Prepare the dataset by placing it in the `data/` directory.
2. Run the data preprocessing and model training script:
    ```bash
    python scripts/train_model.py
    ```
3. The trained model will be saved in the `models/` directory.

### Deploying the Model

1. Start the FastAPI server:
    ```bash
    uvicorn app.main:app --host 0.0.0.0 --port 8000
    ```
2. The API will be accessible at `http://localhost:8000`.

### Docker Deployment

1. Build the Docker image:
    ```bash
    docker build -t customer-churn-prediction .
    ```
2. Run the Docker container:
    ```bash
    docker run -p 8000:8000 customer-churn-prediction
    ```

## API Endpoints

- `POST /predict`: Predict customer churn. Expects a JSON payload with customer features.

