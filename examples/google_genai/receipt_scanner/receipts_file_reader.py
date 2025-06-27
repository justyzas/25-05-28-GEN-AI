import os
from rich import print


FOLDER_PATH = 'C:/Users/Justas PC/Desktop/GEN-AI/25 05 28 GEN-AI su Python OV/resources/cekiai'


def get_all_files():
    files = os.listdir(FOLDER_PATH)
    # Optional: Full paths  
    full_paths = [os.path.join(FOLDER_PATH, f) for f in files]
    return full_paths

def convert_file_to_bytes(file_path: str):
    with open(file_path, 'rb') as f:
      image_bytes = f.read()
    return image_bytes



