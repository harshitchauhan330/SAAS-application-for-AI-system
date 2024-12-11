import joblib
from app.utils.preprocess import preprocess_text

# Load the saved model and vectorizer
model_path = "model/sentiment_model.pkl"
vectorizer_path = "model/vectorizer.pkl"
model = joblib.load(model_path)
vectorizer = joblib.load(vectorizer_path)

# Function to predict sentiment
def predict_sentiment(text: str):
    # Preprocess the input text
    cleaned_text = preprocess_text(text)
    
    # Transform the text into a 2D array using the vectorizer
    vectorized_text = vectorizer.transform([cleaned_text])
    
    # Make predictions using the model
    sentiment_index = model.predict(vectorized_text)[0]
    sentiment_proba = model.predict_proba(vectorized_text)[0]
    confidence = max(sentiment_proba)  # Confidence score

    # Map the sentiment index to a human-readable label
    if sentiment_index == 0:
        sentiment = "negative"
    elif sentiment_index == 1:
        sentiment = "neutral"
    else:
        sentiment = "positive"

    # Return the sentiment and confidence
    return {"sentiment": sentiment, "confidence": confidence}
