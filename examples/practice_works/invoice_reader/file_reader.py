import os
from rich import print

INVOICES_PATH = "C:/Users/kruti/Desktop/GEN AI/25-05-28-GEN-AI/examples/practice_works/data/invoices"


def get_all_files():
    # Gauna visus failus /invoices kataloge ["CONTOSO.pdf", "document (1).pdf"]
    file_names = os.listdir(INVOICES_PATH)
    # Optional: Full paths
    full_paths = [os.path.join(INVOICES_PATH, file_name)
                  for file_name in file_names]
    return full_paths


def convert_file_to_bytes(file_path: str):
    # rb - read binary
    with open(file_path, 'rb') as f:
        file_bytes = f.read()
    return file_bytes


# os.path.join("c:/files/documents/", "document.pdf")====> c:/files/documents/document.pdf
