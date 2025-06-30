from google import genai
from dotenv import load_dotenv
import os
from rich import print
from file_reader import convert_file_to_bytes, get_all_files
from schema import InvoiceModel
from google.genai import types
import mimetypes
load_dotenv()

GOOGLE_AI_KEY = os.getenv("GOOGLE_API_TOKEN")
MODEL="gemini-2.5-flash"

client = genai.Client(api_key=GOOGLE_AI_KEY)



file_paths = get_all_files()
files = [{"bytes": convert_file_to_bytes(file_path), "mime": mimetypes.guess_type(file_path)[0]} for file_path in file_paths]

 
all_files_bytes_request = [
    types.Part.from_bytes(data=file["bytes"], mime_type=file["mime"]) 
    for file in files
    ]

# Modelio užklausimas
response = client.models.generate_content(
    model=MODEL,
    contents=[
        "Your job is to read all the receipts, and provide me with the json.", 
    ] + all_files_bytes_request,
    config={
        "response_mime_type": "application/json",
        "response_schema": list[InvoiceModel],
    }
)
