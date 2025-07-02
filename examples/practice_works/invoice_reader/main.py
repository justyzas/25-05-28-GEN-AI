from google import genai
from dotenv import load_dotenv
import os
from rich import print
from file_reader import convert_file_to_bytes, get_all_files
from schema import InvoiceModel
from google.genai import types
import mimetypes
from csv_generator import write_structured_invoice_output_to_csv as output_csv
from filter import filter_invoices, filter_non_invoices
import shutil
from logger import log

load_dotenv()

INVOICES_PATH = "C:/Users/kruti/Desktop/GEN AI/25-05-28-GEN-AI/examples/practice_works/data/invoices"
PROCESSED_PATH = "C:/Users/kruti/Desktop/GEN AI/25-05-28-GEN-AI/examples/practice_works/data/processed"
OTHER_PATH = "C:/Users/kruti/Desktop/GEN AI/25-05-28-GEN-AI/examples/practice_works/data/other"

GOOGLE_AI_KEY = os.getenv("GOOGLE_API_TOKEN")
MODEL = "gemini-2.5-flash"

log("Config loaded")

client = genai.Client(api_key=GOOGLE_AI_KEY)
log("Client initialized")

# Gauname visų failų kelius (["c:/path/to/pdfdoc1.pdf", "c:/path/to/pdfdoc2.pdf".....])
file_paths = get_all_files()

# [{ "bytes": 0xcfaaab6546, "mime": "application/pdf"}, {}]
files = [{"bytes": convert_file_to_bytes(file_path), "mime": mimetypes.guess_type(
    file_path)[0], "filename": os.path.basename(file_path)} for file_path in get_all_files()]
log("Files converted to bytes successfully")
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

log("Sending request to LLM service")
# Modelio užklausimas
response = client.models.generate_content(
    model=MODEL,
    contents=[
        "Your job is to read all the invoices, and provide me with the json. If invoice does not have an invoice number, treat it as non invoice. Non invoices should also be returned as objects in same list."
    ] + all_files_bytes_request,
    config={
        "response_mime_type": "application/json",
        "response_schema": list[InvoiceModel],
    }
)

log("Got a response from LLM service successfully")
# [doc1info, doc2info]
invoices_and_other: list[InvoiceModel] = response.parsed

# Failo pavadinimo priskyrimas sąskaitoms (jau apdorotms)
for index in range(len(invoices_and_other)):
    invoices_and_other[index].original_file_name = files[index]["filename"]

invoices = filter_invoices(invoices_and_other)
non_invoices = filter_non_invoices(invoices_and_other)

log(f"GOT invoices: {len(invoices)}, non-invoices: {len(non_invoices)}")
log("Outputting data to CSV...")
output_csv(invoices)
log("CSV Output succesful!")
log("Transferring files to their directories...")

for invoice in invoices:
    source_path = os.path.join(INVOICES_PATH, invoice.original_file_name)
    # C:/Users/kruti/Desktop/GEN AI/25-05-28-GEN-AI/examples/practice_works/data/invoices/CONTOSO.pdf
    destination_path = os.path.join(PROCESSED_PATH, invoice.original_file_name)
    # C:/Users/kruti/Desktop/GEN AI/25-05-28-GEN-AI/examples/practice_works/data/processed/CONTOSO.pdf
    log(f"Transferring {source_path} to {destination_path}")
    shutil.move(source_path, destination_path)
    log("Transfer succesful!")

for non_invoice in non_invoices:
    source_path = os.path.join(INVOICES_PATH, non_invoice.original_file_name)
    # C:/Users/kruti/Desktop/GEN AI/25-05-28-GEN-AI/examples/practice_works/data/invoices/CONTOSO.pdf
    destination_path = os.path.join(OTHER_PATH, non_invoice.original_file_name)
    # C:/Users/kruti/Desktop/GEN AI/25-05-28-GEN-AI/examples/practice_works/data/other/CONTOSO.pdf
    log(f"Transferring {source_path} to {destination_path}")
    shutil.move(source_path, destination_path)
    log("Transfer succesful!")

log("Program ended it's job!")
