from fastapi import APIRouter
from pydantic import BaseModel
import joblib
import re

# Load the trained model and vectorizer
model = joblib.load("model/sentiment_model.pkl")
vectorizer = joblib.load("model/vectorizer.pkl")

# Router instance
router = APIRouter()

# Define input and output schemas
class SentimentRequest(BaseModel):
    text: str

class SentimentResponse(BaseModel):
    sentiment: str
    confidence: list

# Function to clean and preprocess the text
def preprocess_text(text):
    # Clean the text by removing non-alphabetical characters and making it lowercase
    text = re.sub(r"http\S+", "", text)  # Remove URLs
    text = re.sub(r"@\w+", "", text)  # Remove Twitter mentions (@username)
    text = re.sub(r"[^a-zA-Z\s]", "", text)  # Remove special characters
    text = text.lower()  # Convert text to lowercase
    return text

# Endpoint to predict sentiment
@router.post("/predict", response_model=SentimentResponse)
def predict_sentiment_api(request: SentimentRequest):
    # Preprocess the input text
    cleaned_text = preprocess_text(request.text)

    # Transform the text using the vectorizer
    vectorized_text = vectorizer.transform([cleaned_text])

    # Predict sentiment
    sentiment = model.predict(vectorized_text)[0]
    confidence = model.predict_proba(vectorized_text)[0]

    # Return the response as sentiment and confidence
    return SentimentResponse(sentiment=str(sentiment), confidence=confidence.tolist())
