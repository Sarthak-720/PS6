from flask import Flask, request, render_template, redirect, url_for
import os
from OCR import extract_details
from llm_integration import (
    validate_gst_certificate,
    validate_invoice_data,
    validate_pan_card,
    validate_bol,
    validate_export_declaration,
)

app = Flask(__name__)
app.config["UPLOAD_FOLDER"] = r"C:\Hack1\uploads"
os.makedirs(app.config["UPLOAD_FOLDER"], exist_ok=True)

# Route: Home Page (Document Selection)
@app.route("/", methods=["GET", "POST"])
def home():
    return render_template("home.html")


# Common File Upload Route
@app.route("/upload/<doc_type>", methods=["GET", "POST"])
def upload_file(doc_type):
    if request.method == "POST":
        file = request.files.get("file")
        if not file or file.filename == "":
            return "No file uploaded"
        
        file_path = os.path.join(app.config["UPLOAD_FOLDER"], file.filename)
        file.save(file_path)
        return redirect(url_for("process_file", doc_type=doc_type, file_name=file.filename))
    
    return render_template("upload.html", doc_type=doc_type)


# Route: Process File Based on Document Type
@app.route("/process/<doc_type>/<file_name>", methods=["GET", "POST"])
def process_file(doc_type, file_name):
    file_path = os.path.join(app.config["UPLOAD_FOLDER"], file_name)

    if request.method == "POST":
        edited_details = request.form["extracted_details"]
        validation_feedback = process_validation(doc_type, edited_details)  # Get formatted feedback

        # Save the edited file
        edited_file_path = os.path.join(app.config["UPLOAD_FOLDER"], f"edited_{file_name}.txt")
        with open(edited_file_path, "w", encoding="utf-8") as f:
            f.write(edited_details)

        return render_template(
            "validation_feedback.html",
            file_name=file_name,
            edited_details=edited_details,
            feedback=validation_feedback,  # Pass formatted feedback
        )

    # Extract details based on doc_type
    extracted_text = extract_details(file_path)
    return render_template("edit.html", details=extracted_text, file_name=file_name, doc_type=doc_type)

def process_validation(doc_type, extracted_text):
    validation_functions = {
        "gst_certificate": validate_gst_certificate,
        "invoice": validate_invoice_data,
        "pan_card": validate_pan_card,
        "bol": validate_bol,
        "export_declaration": validate_export_declaration,
    }
    
    validation_func = validation_functions.get(doc_type)
    feedback = validation_func(extracted_text) if validation_func else "Invalid document type"
    
    # Format the feedback to replace newlines with <br> for proper HTML rendering
    return format_feedback(feedback)

def format_feedback(feedback_text):
    """
    Formats the feedback text by replacing newlines with <br> tags.
    This allows HTML rendering of the response.
    """
    return feedback_text.replace("\n", "<br>")

if __name__ == "__main__":
    app.run(debug=True)