import pandas as pd
import json
import os
from docx import Document

def convert_csv_to_json(csv_file, json_file):
    df = pd.read_csv(csv_file)
    df.to_json(json_file, orient='records', indent=4)
    print(f"CSV converted to JSON: {json_file}")

def convert_excel_to_json(excel_file, json_file, sheet_name=0):
    df = pd.read_excel(excel_file, sheet_name=sheet_name)
    df.to_json(json_file, orient='records', indent=4)
    print(f"Excel converted to JSON: {json_file}")

def convert_docx_to_json(docx_file, json_file):
    doc = Document(docx_file)
    data = [para.text.strip() for para in doc.paragraphs if para.text.strip()]
    with open(json_file, 'w', encoding='utf-8') as f:
        json.dump({"paragraphs": data}, f, indent=4)
    print(f"Word document converted to JSON: {json_file}")

# Example usage
file_type = input("Enter file type (csv, excel, word): ").strip().lower()
input_file = input("Enter input file path: ").strip()
output_file = input("Enter output JSON file name (e.g., output.json): ").strip()

if file_type == 'csv':
    convert_csv_to_json(input_file, output_file)
elif file_type == 'excel':
    convert_excel_to_json(input_file, output_file)
elif file_type == 'word':
    convert_docx_to_json(input_file, output_file)
else:
    print("Unsupported file type.")