from google import genai
from dotenv import load_dotenv
import os
from rich import print
from file_reader import convert_file_to_bytes, get_all_files
from schema import InvoiceModel
from google.genai import types
import mimetypes
from csv_generator import write_structured_invoice_output_to_csv as output_csv

load_dotenv()

GOOGLE_AI_KEY = os.getenv("GOOGLE_API_TOKEN")
MODEL = "gemini-2.5-flash"

client = genai.Client(api_key=GOOGLE_AI_KEY)


# Gauname visų failų kelius (["c:/path/to/pdfdoc1.pdf", "c:/path/to/pdfdoc2.pdf".....])
file_paths = get_all_files()

# [{ "bytes": 0xcfaaab6546, "mime": "application/pdf"}, {}]
files = [{"bytes": convert_file_to_bytes(file_path), "mime": mimetypes.guess_type(
    file_path)[0]} for file_path in get_all_files()]

# Sugeneruojami failų objektai, kuriuos supranta gemini
#  Part(
#         video_metadata=None,
#         thought=None,
#         inline_data=Blob(display_name=None, data=b'%PDF-1.7 failo turinys', mime_type='application/pdf'),
#         file_data=None,
#         thought_signature=None,
#         code_execution_result=None,
#         executable_code=None,
#         function_call=None,
#         function_response=None,
#         text=None
#     )
all_files_bytes_request = [types.Part.from_bytes(
    data=file["bytes"], mime_type=file["mime"]) for file in files]

# Modelio užklausimas
response = client.models.generate_content(
    model=MODEL,
    contents=[
        "Your job is to read all the invoices, and provide me with the json. If invoice does not have an invoice number, treat it as non invoice"
    ] + all_files_bytes_request,
    config={
        "response_mime_type": "application/json",
        "response_schema": list[InvoiceModel],
    }
)

invoices = response.parsed

print(invoices)
output_csv(invoices)
