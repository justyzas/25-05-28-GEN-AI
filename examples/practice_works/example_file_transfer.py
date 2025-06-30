import shutil

source_path = "data/invoices/CONTOSO.pdf"
destination_path = "data/processed/CONTOSO.pdf"

shutil.move(source_path, destination_path)