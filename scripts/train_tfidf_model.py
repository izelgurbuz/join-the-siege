
import os
import pickle
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

# Synthetic sample data
texts = [
    "This is a driver's license document",
    "Bank statement showing account details",
    "Invoice for purchased products",
    "Generic document without clear category"
]
labels = [
    "drivers_licence",
    "bank_statement",
    "invoice",
    "unknown file"
]

# Create TF-IDF vectorizer
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(texts)

# Train Logistic Regression model
model = LogisticRegression()
model.fit(X, labels)

# Make sure models directory exists
os.makedirs('models', exist_ok=True)

# Save vectorizer and model together
with open('models/tfidf_model.pkl', 'wb') as f:
    pickle.dump((vectorizer, model), f)

print("✅ Model saved to models/tfidf_model.pkl")
