import google.generativeai as genai
from html import escape
import json
import os
import pypdf

document_dir = r"C:\Users\Anirudh\Desktop\IITM\INTERN\document_scan"

def organise_details(text):
    """
    This function organizes the extracted text into a dictionary.
    """
    organized_details = text
    return organized_details

def generate_llm_response(prompt):
    """
    Generates a response using Gemini LLM based on the provided prompt.
    """
    genai.configure(api_key="AIzaSyDLvYXhcoSGk1uzik08RXmyx1x9h8OatzI")

    model = genai.GenerativeModel(
        model_name="gemini-1.5-flash",
        generation_config={
            "temperature": 0.4,
            "top_p": 0.9,
            "top_k": 40,
            "max_output_tokens": 2048,
            "response_mime_type": "text/plain",
        },
    )

    chat_session = model.start_chat(history=[])
    response = chat_session.send_message(prompt)
    
    # Ensure response is in text format, assuming candidates[0].content is a string
    response_text = str(response.candidates[0].content).strip()  # Convert to string and remove extra spaces
    return response_text



def format_response(response_text):
    """
    Formats the LLM-generated response for better readability by ensuring newlines are properly handled
    and markdown-like formatting is respected.
    """
    # formatted_response = escape(response_text).replace("\n", "<br>").replace("**", "<b>").replace("*", "")
    formatted_response = escape(response_text).replace('\\"', '"').replace("\\'", "'")
    return formatted_response

# Validation Functions

def validate_gst_certificate(extracted_text):


    gst_dir = r"C:\Hack1\ref_doc\gst_certificate.pdf"

    try:
        # Initialize PdfReader with the file path
        pdf_reader = pypdf.PdfReader(gst_dir)

        # Extract text from all pages
        text = ""
        for page in pdf_reader.pages:
            text += page.extract_text()
    
    except FileNotFoundError:
        print("The file was not found.")
    except Exception as e:
        print(f"Error reading the PDF: {e}")

    """
    Validates a GST Certificate using Gemini LLM for compliance checks.
    """
    prompt = f"""
    You are a GST compliance expert. Analyze the following GST certificate data for accuracy:

    {extracted_text}

    refer to the rules and regulations mentioned in this text

    {text}
    
    Format the response in sections, using bullet points and line breaks where needed. and limit the output to 100 words
    """
    response = generate_llm_response(prompt)
    return format_response(response)


def validate_invoice_data(extracted_text):
    
    inv_dir = r"C:\Hack1\ref_doc\invoice.pdf"

    try:
        # Initialize PdfReader with the file path
        pdf_reader = pypdf.PdfReader(inv_dir)

        # Extract text from all pages
        text = ""
        for page in pdf_reader.pages:
            text += page.extract_text()
    
    except FileNotFoundError:
        print("The file was not found.")
    except Exception as e:
        print(f"Error reading the PDF: {e}")

    
    """
    Validates invoice details using Gemini LLM for proper customs and tax compliance.
    """
    prompt = f"""
    You are a customs and tax compliance expert. Review the following invoice data for accuracy:

    {extracted_text}
    
    refer to the rules and regulations mentioned in this text

    {text}
    
    Format the response in structured sections using bullet points and line breaks. and limit the output to 100 words
    """
    response = generate_llm_response(prompt)
    return format_response(response)


def validate_pan_card(extracted_text):
    pan_dir = r"C:\Hack1\ref_doc\pan_card.pdf"

    try:
        # Initialize PdfReader with the file path
        pdf_reader = pypdf.PdfReader(pan_dir)

        # Extract text from all pages
        text = ""
        for page in pdf_reader.pages:
            text += page.extract_text()
    
    except FileNotFoundError:
        print("The file was not found.")
    except Exception as e:
        print(f"Error reading the PDF: {e}")
    
    """
    Validates PAN card details for correctness using Gemini LLM.
    """
    prompt = f"""
    You are an identity verification expert. Verify the following PAN card details:

    {extracted_text}

    refer to the rules and regulations mentioned in this text

    {text}

    Format the response clearly using bullet points and line breaks. and limit the output to 100 words
    """
    response = generate_llm_response(prompt)
    return format_response(response)


def validate_bol(extracted_text):
    bol_dir = r"C:\Hack1\ref_doc\bol.pdf"

    try:
        # Initialize PdfReader with the file path
        pdf_reader = pypdf.PdfReader(bol_dir)

        # Extract text from all pages
        text = ""
        for page in pdf_reader.pages:
            text += page.extract_text()
    
    except FileNotFoundError:
        print("The file was not found.")
    except Exception as e:
        print(f"Error reading the PDF: {e}")
    
    """
    Validates Bill of Lading data for shipping and customs compliance.
    """
    prompt = f"""
    You are a logistics and customs compliance expert. Review the following Bill of Lading data for accuracy:

    {extracted_text}

    refer to the rules and regulations mentioned in this text

    {text}

    Format the response using bullet points and clear sections. and limit the output to 100 words
    """
    response = generate_llm_response(prompt)
    return format_response(response)


def validate_export_declaration(extracted_text):
    exp_dir = r"C:\Hack1\ref_doc\export_declaration.pdf"

    try:
        # Initialize PdfReader with the file path
        pdf_reader = pypdf.PdfReader(exp_dir)

        # Extract text from all pages
        text = ""
        for page in pdf_reader.pages:
            text += page.extract_text()
    
    except FileNotFoundError:
        print("The file was not found.")
    except Exception as e:
        print(f"Error reading the PDF: {e}")
    
    """
    Validates Export Declaration details for international shipping compliance.
    """
    prompt = f"""
    You are an export documentation compliance expert. Review the following Export Declaration data for accuracy:

    {extracted_text}

    refer to the rules and regulations mentioned in this text

    {text}

    Format the response using structured sections, bullet points, and line breaks. and limit the output to 100 words
    """
    response = generate_llm_response(prompt)
    return format_response(response)
