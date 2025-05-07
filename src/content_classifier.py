import pickle
import PyPDF2

def extract_pdf_text(file):
    reader = PyPDF2.PdfReader(file)
    text = " ".join(page.extract_text() or '' for page in reader.pages)
    return text

# Load pretrained synthetic model
with open('models/tfidf_model.pkl', 'rb') as f:
    vectorizer, model = pickle.load(f)

def classify_by_content(file):
    file.seek(0)  # reset file pointer
    text = extract_pdf_text(file)

    if not text.strip():
        return "unknown file"

    X = vectorizer.transform([text])
    prediction = model.predict(X)[0]
    return prediction
