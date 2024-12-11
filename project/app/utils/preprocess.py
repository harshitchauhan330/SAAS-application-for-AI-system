import re

# Text preprocessing function
def preprocess_text(text: str) -> str:
    # Remove URLs
    text = re.sub(r"http\S+", "", text)
    # Remove mentions (e.g., @username)
    text = re.sub(r"@\w+", "", text)
    # Remove special characters and digits
    text = re.sub(r"[^a-zA-Z\s]", "", text)
    # Convert to lowercase
    return text.lower().strip()
