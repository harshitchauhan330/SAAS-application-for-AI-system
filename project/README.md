# Sentiment Analysis SaaS Application

This project implements a SaaS application for sentiment analysis using FastAPI. It uses a pre-trained machine learning model to classify text as positive, negative, or neutral sentiment. The application is containerized using Docker for easy deployment and scalability.

---

## Table of Contents
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Folder Structure](#folder-structure)
- [Setup and Deployment](#setup-and-deployment)
- [API Documentation](#api-documentation)
- [Testing the Application](#testing-the-application)
- [Future Improvements](#future-improvements)

---

## Features
- RESTful API for sentiment prediction.
- Pre-trained machine learning model (`LogisticRegression`) with `scikit-learn`.
- FastAPI-based framework with Swagger and ReDoc documentation.
- Dockerized for easy deployment and scalability.

---

## Technologies Used
- **Python 3.10**
- **FastAPI** for building the REST API.
- **scikit-learn** for the sentiment classification model.
- **Docker** for containerization.
- **MLFlow** for model versioning (optional).
- **Postman** for API testing.

---

## Folder Structure


---

## Setup and Deployment

### Prerequisites
- Python 3.10 installed on your system.
- Docker installed and running.

### Running Locally

Create a virtual environment:

**python -m venv venv**
source venv/bin/activate  # For Windows: venv\Scripts\activate
Install dependencies:
 
**pip install -r requirements.txt**
Run the FastAPI application:

**uvicorn app.main:app --reload**
Access the API Documentation:

Swagger UI: http://127.0.0.1:8000/docs
ReDoc: http://127.0.0.1:8000/redoc
Running with Docker
Build the Docker image:
  
docker build -t sentiment-analysis-app .
Run the Docker container:
  
docker run -d -p 8000:8000 sentiment-analysis-app
Access the API:

Swagger UI: http://127.0.0.1:8000/docs
ReDoc: http://127.0.0.1:8000/redoc
API Documentation
Endpoint: /api/v1/predict
Method: POST
Description: Predicts the sentiment of the input text.
Request Body:
json
  
{
    "text": "I absolutely love this movie!"
}
Response:
json
  
{
    "sentiment": "positive",
    "confidence": 0.86146022
}
### Testing the Application
Run the test script locally:

 
  
**python tests/test_model.py**
Enter a text input to analyze its sentiment.
Example output:
  
  
Enter a text to analyze sentiment: I absolutely love this movie!
Predicted sentiment: positive
Prediction probabilities: 0.86146022
Use Postman for API testing:

Set the method to POST.
URL: http://127.0.0.1:8000/api/v1/predict.
Payload:
json
  
{
    "text": "This movie was fantastic!"
}
### Future Improvements
- Add user authentication for API access.
- Implement model versioning and tracking with MLFlow.
- Use Kubernetes for scaling the application.
- Upgrade the model to a deep learning-based architecture.
- Enable batch processing for multiple text inputs.
