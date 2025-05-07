from werkzeug.datastructures import FileStorage
from src.content_classifier import classify_by_content

def classify_file(file: FileStorage):
    filename = file.filename.lower()

    if "drivers_license" in filename:
        return "drivers_licence"

    if "bank_statement" in filename:
        return "bank_statement"

    if "invoice" in filename:
        return "invoice"

    # fallback to content-based classification
    return classify_by_content(file)
