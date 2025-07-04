from fastapi import FastAPI
from models import ItemModel
from initializer import collect_starting_data
from product_registrator import save_product_to_file
app = FastAPI()


# RAM atmintis (Labai laikina)
products: list[ItemModel] = collect_starting_data()

# CRUD
# C - Create
# R - Read

# U - Update
# D - Delete


@app.get("/")
def ifgkhudjsanfpjkhgsdfgjsdjhfgvsdjfbc():
    return "Labas Pasauli :)"


@app.get("/products")
def get_all_products() -> list[ItemModel]:
    return products


@app.post("/products")
def create_new_product(new_product: ItemModel):
    products.append(new_product)
    save_product_to_file(new_product)
    return {"message": "New product was successfully added to your shop! :)"}


@app.get("/json")
def ifgkhudjsanfpjkhgsdfgjsdjhfgsdjfba():
    return {"name": "Petras", "email": "petras@jonaitis.lt", "age": 27}


@app.get("/number-of-files-in-system")
def ifgkhudjsanfpjkhgsdfajsdjhfgsdjfba():
    return 4
