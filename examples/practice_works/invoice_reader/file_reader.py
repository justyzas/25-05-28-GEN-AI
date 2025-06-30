import os
from rich import print

INVOICES_PATH = "C:/Users/Justas PC/Desktop/GEN-AI/25 05 28 GEN-AI su Python OV/examples/practice_works/data/invoices"

def get_all_files():
    files = os.listdir(INVOICES_PATH)
    # Optional: Full paths  
    full_paths = [os.path.join(INVOICES_PATH, f) for f in files]
    return full_paths

def convert_file_to_bytes(file_path: str):
    with open(file_path, 'rb') as f:
      image_bytes = f.read()
    return image_bytes