import joblib
import re
import numpy as np

# Load the trained model and vectorizer
model = joblib.load("model/sentiment_model.pkl")
vectorizer = joblib.load("model/vectorizer.pkl")  # Load the vectorizer used during training

# Function to clean and preprocess the text
def preprocess_text(text):
    # Clean the text by removing non-alphabetical characters and making it lowercase
    text = re.sub(r"http\S+", "", text)  # Remove URLs
    text = re.sub(r"@\w+", "", text)  # Remove Twitter mentions (@username)
    text = re.sub(r"[^a-zA-Z\s]", "", text)  # Remove special characters
    text = text.lower()  # Convert text to lowercase
    return text

# Function to test sentiment analysis
def test_sentiment_analysis(text):
    # Preprocess the input text
    cleaned_text = preprocess_text(text)

    # Transform the text using the vectorizer
    vectorized_text = vectorizer.transform([cleaned_text])

    # Predict sentiment
    sentiment = model.predict(vectorized_text)
    confidence = model.predict_proba(vectorized_text)

    # Output the results
    print(f"Predicted sentiment: {sentiment[0]}")
    print(f"Prediction probabilities: {confidence[0]}")

    return sentiment[0], confidence[0]

# Take user input for testing
if __name__ == "__main__":
    user_input = input("Enter a text to analyze sentiment: ")
    sentiment, confidence = test_sentiment_analysis(user_input)
    print(f"Sentiment: {sentiment}, Confidence: {confidence}")
