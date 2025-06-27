# GOOGLE MODULE TO WORK WITH GEN AI
from google import genai
from google.genai import types

#COMMON MODULES
from dotenv import load_dotenv
import os
from rich import print

#MY OWN MODULES
from receipts_file_reader import get_all_files, convert_file_to_bytes
from data_schema import ReceiptInformation
from output_json import output_result_json

# Initialize
load_dotenv()
GOOGLE_AI_KEY = os.getenv("GOOGLE_API_TOKEN")
MODEL="gemini-2.5-flash"

client = genai.Client(api_key=GOOGLE_AI_KEY)

# Gauname failu sarašą baitų formatu:
all_files = get_all_files()
all_files_bytes = [convert_file_to_bytes(file_path) for file_path in all_files]

all_files_bytes_request = [
    types.Part.from_bytes(data=file_bytes, mime_type='image/jpeg') 
    for file_bytes in all_files_bytes
    ]

# Modelio užklausimas
response = client.models.generate_content(
    model=MODEL,
    contents=[
        "Your job is to read all the receipts, and provide me with the json.", 
    ] + all_files_bytes_request,
    config={
        "response_mime_type": "application/json",
        "response_schema": list[ReceiptInformation],
    }
)

output_result_json(response.parsed)
print("[green]Receipt information succesfuly parsed to [boldgreen]output.json[/boldgreen][/green]")