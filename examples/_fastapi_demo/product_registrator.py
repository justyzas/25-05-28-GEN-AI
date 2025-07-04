from models import ItemModel


PATH_TO_DB = "C:/Users/kruti/Desktop/GEN AI/25-05-28-GEN-AI/examples/_fastapi_demo/product_database.csv"


def save_product_to_file(item: ItemModel):
    with open(PATH_TO_DB, "a", encoding="utf-8-sig") as f:
        f.write(
            f"\n{item.name},{item.price},{item.weight},{item.quantity_in_stock}")
