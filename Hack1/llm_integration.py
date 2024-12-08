import google.generativeai as genai
from html import escape
import json

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
    """
    Validates a GST Certificate using Gemini LLM for compliance checks.
    """
    prompt = f"""
    You are a GST compliance expert. Analyze the following GST certificate data for accuracy:

    {extracted_text}

    Tasks (Provide a structured response with appropriate sections):
    - **GSTIN Verification:** Validate the correctness of the GSTIN number format.
    - **Business Details Check:** Verify registered business name, address, and legal status.
    - **Registration Date and Type:** Ensure the registration date and business type match records.
    - **Tax Category Verification:** Confirm applicable tax categories (CGST, SGST, IGST).
    - **Compliance Issues:** Highlight any missing or incorrect information.
    
    Format the response in sections, using bullet points and line breaks where needed. and limit the output to 100 words
    """
    response = generate_llm_response(prompt)
    return format_response(response)


def validate_invoice_data(extracted_text):
    """
    Validates invoice details using Gemini LLM for proper customs and tax compliance.
    """
    prompt = f"""
    You are a customs and tax compliance expert. Review the following invoice data for accuracy:

    {extracted_text}

    Tasks (Provide a structured response with appropriate sections):
    - **Invoice Number and Date:** Ensure the presence of an invoice number and date.
    - **Buyer and Seller Details:** Verify names, addresses, and tax registration numbers.
    - **Product Details:** Validate product names, quantities, unit prices, and tax rates.
    - **HSN/SAC Code Matching:** Check HSN/SAC codes for correct classification.
    - **Tax Calculations:** Confirm the accuracy of tax calculations.
    - **Compliance Check:** Identify missing or incorrect data and suggest corrections.

    Format the response in structured sections using bullet points and line breaks. and limit the output to 100 words
    """
    response = generate_llm_response(prompt)
    return format_response(response)


def validate_pan_card(extracted_text):
    """
    Validates PAN card details for correctness using Gemini LLM.
    """
    prompt = f"""
    You are an identity verification expert. Verify the following PAN card details:

    {extracted_text}

    Tasks (Provide a structured response with appropriate sections):
    - **PAN Format Check:** Ensure the PAN follows the standard alphanumeric format (AAAAA1234A).
    - **Name and DOB Verification:** Validate the person's name and date of birth against known formats.
    - **Father's Name Check:** Ensure father's name is present and correctly spelled.
    - **Document Integrity:** Check for any signs of tampering or incomplete data.

    Format the response clearly using bullet points and line breaks. and limit the output to 100 words
    """
    response = generate_llm_response(prompt)
    return format_response(response)


def validate_bol(extracted_text):
    """
    Validates Bill of Lading data for shipping and customs compliance.
    """
    prompt = f"""
    You are a logistics and customs compliance expert. Review the following Bill of Lading data for accuracy:

    {extracted_text}

    Tasks (Provide a structured response with appropriate sections):
    - **Shipper and Consignee Details:** Verify names, addresses, and contact information.
    - **Cargo Description:** Ensure cargo details, weight, and dimensions match industry standards.
    - **Container Number and Seal Details:** Confirm that the container numbers and seal details are valid.
    - **Port and Delivery Information:** Check ports of loading, discharge, and delivery addresses.
    - **Document Integrity:** Identify missing or incorrect data and recommend corrections.

    Format the response using bullet points and clear sections. and limit the output to 100 words
    """
    response = generate_llm_response(prompt)
    return format_response(response)


def validate_export_declaration(extracted_text):
    """
    Validates Export Declaration details for international shipping compliance.
    """
    prompt = f"""
    You are an export documentation compliance expert. Review the following Export Declaration data for accuracy:

    {extracted_text}

    Tasks (Provide a structured response with appropriate sections):
    - **Exporter and Importer Details:** Validate exporter and importer names, addresses, and contact information.
    - **Export License Verification:** Ensure the export license number is correct and valid.
    - **Product Description:** Check product descriptions, HS codes, and export quantities.
    - **Shipping and Delivery Details:** Confirm accurate shipping terms, delivery addresses, and ports of entry.
    - **Customs Declarations:** Validate declarations against international trade compliance requirements.
    - **Compliance Check:** Highlight missing or incorrect data and suggest corrections.

    Format the response using structured sections, bullet points, and line breaks. and limit the output to 100 words
    """
    response = generate_llm_response(prompt)
    return format_response(response)
