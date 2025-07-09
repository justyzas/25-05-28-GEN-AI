from fastapi import FastAPI, HTTPException
from models import ItemModel
from initializer import collect_starting_data
from product_registrator import save_product_to_file
app = FastAPI()

# 1. DB
# 2. Jupyter
# 3. Fine-Tuning

# RAM atmintis (Labai laikina)
products: list[ItemModel] = collect_starting_data()

# CRUD
# C - Create
# R - Read
# U - Update
# D - Delete

# DOCS on status codes: https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Status#informational_responses
# 1XX - Informational responses
# 2XX - Success
# 3XX - Redirections
# 4XX - Client side error
# 5XX - Server side error

# Body (didelis objektas su informacija)
# Dinaminiai route segmentai
# Query parameters - parametrai, neįvardinti route segmentuose, tačiau esantys funkcijoje kaip parametrai.
# /products?page=1

# https://www.w3schools.com/mysql/trymysql.asp?filename=trysql_select_limit_offset


@app.get("/products")
def get_all_products(page: int) -> list[ItemModel]:
    return products[(page-1)*5:page*5]

# Įprastai teigiamo atsakymo status code

# Request body - Užklausos kūnas. Jis privalo būti sudarytas iš modelio (klasės)

# https://www.w3schools.com/sql/sql_insert.asp#gsc.tab=0


@app.post("/products", status_code=201)
def create_new_product(new_product: ItemModel):
    products.append(new_product)
    save_product_to_file(new_product)
    return {"message": "New product was successfully added to your shop! :)"}

# Dinaminis route segmentas (parametras)


@app.get("/products/{id}")
def get_single_product(id: int):
    for product in products:
        if product.id == id:
            return product
    # Atsakymas su neįprastu status code. (kai nepavyksta apdoroti užklausos)
    raise HTTPException(status_code=404, detail="Product was not found")


@app.put("/products/{id}")
def update_single_product(id: int, updated_product: ItemModel):
    index = 0
    for product in products:
        if product.id == id:
            products[index] = updated_product
            return products[index]
        index += 1
    raise HTTPException(status_code=404, detail="Product was not found")


@app.delete("/products/{id}", status_code=204)
def delete_single_product(id: int):
    for product in products:
        if product.id == id:
            products.remove(product)
            return
    # Atsakymas su neįprastu status code. (kai nepavyksta apdoroti užklausos)
    raise HTTPException(status_code=404, detail="Product was not found")


@app.get("/json")
def ifgkhudjsanfpjkhgsdfgjsdjhfgsdjfba():
    return {"name": "Petras", "email": "petras@jonaitis.lt", "age": 27}


@app.get("/number-of-files-in-system")
def ifgkhudjsanfpjkhgsdfajsdjhfgsdjfba():
    return 4
