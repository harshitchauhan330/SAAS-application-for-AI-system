from fastapi import FastAPI
from app.routes import sentiment

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome to the Sentiment Analyzer!"}

# Include routes for sentiment analysis
app.include_router(sentiment.router, prefix="/api/v1")
