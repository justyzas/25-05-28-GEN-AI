from models import ItemModel
from rich import print
PATH_TO_DB = "C:/Users/kruti/Desktop/GEN AI/25-05-28-GEN-AI/examples/_fastapi_demo/product_database.csv"


def collect_starting_data():
    with open(PATH_TO_DB, "r", encoding="utf-8-sig") as f:
        products_csv = f.read()
    products_str_list = products_csv.split("\n")  # \n - naujos eilute simbolis

    product_list: list[ItemModel] = []
    for product_str in products_str_list:
        # Išskaidome produkto teksto eilutę per kablelius
        product_parts = product_str.split(",")
        # Sudarome produckto modelį iš aatskirto produkto teksto per kablelius
        product = ItemModel(id=product_parts[0], name=product_parts[1], price=float(product_parts[2]), weight=float(
            product_parts[3]), quantity_in_stock=int(product_parts[4]))
        # Modelį pridedame prie bendro produktų sąrašo
        product_list.append(product)
    return product_list
