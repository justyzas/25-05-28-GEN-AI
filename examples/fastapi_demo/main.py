from fastapi import FastAPI, HTTPException
from models import ItemModel, ItemCreateModel, ItemUpdateModel
from initializer import collect_starting_data
from product_registrator import save_product_to_file
import sqlite3

# Prisijungimas prie duomenų bazės
con = sqlite3.connect("tutorial.db")
cursor = con.cursor()


# Sukuria lentelę Products
cursor.execute("""CREATE TABLE IF NOT EXISTS Products (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    price DECIMAL(10, 2),
    weight DECIMAL(6, 2),
    quantity_in_stock INT
);""")

app = FastAPI()


# 1. DB
# 2. Jupyter
# 3. Fine-Tuning

# RAM atmintis (Labai laikina)
# products: list[ItemModel] = collect_starting_data()

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


@app.get("/products")  # Gauti visus produktus
def get_all_products(page: int = 1, products_per_page: int = 5) -> list[ItemModel]:
    with sqlite3.connect("tutorial.db") as con:
        # con.row_factory = sqlite3.Row
        cursor = con.cursor()
        cursor.execute(
            f"""SELECT * FROM Products LIMIT {products_per_page} OFFSET {(page-1)*products_per_page};""")
        products = cursor.fetchall()
    products_res = [ItemModel(id=product[0], name=product[1], price=product[2],
                              weight=product[3], quantity_in_stock=product[4]) for product in products]
    return products_res

# Įprastai teigiamo atsakymo status code

# Request body - Užklausos kūnas. Jis privalo būti sudarytas iš modelio (klasės)

# https://www.w3schools.com/sql/sql_insert.asp#gsc.tab=0


@app.post("/products", status_code=201)
def create_new_product(new_product: ItemCreateModel):
    with sqlite3.connect("tutorial.db") as con:
        cursor = con.cursor()
        cursor.execute(f"""INSERT INTO Products (name, price, weight, quantity_in_stock)
        VALUES ('{new_product.name}', {new_product.price}, {new_product.weight}, {new_product.quantity_in_stock});""")
    return {"message": "New product was successfully added to your shop! :)"}

# Dinaminis route segmentas (parametras)


@app.get("/products/{id}")
def get_single_product(id: int):
    with sqlite3.connect("tutorial.db") as con:
        # con.row_factory = sqlite3.Row
        cursor = con.cursor()
        cursor.execute(
            f"""SELECT * FROM Products WHERE id = {id};""")
        products = cursor.fetchall()
    if len(products) != 0:
        product = products[0]
        return ItemModel(id=product[0], name=product[1], price=product[2],
                         weight=product[3], quantity_in_stock=product[4])
    # Atsakymas su neįprastu status code. (kai nepavyksta apdoroti užklausos)
    raise HTTPException(status_code=404, detail="Product was not found")


@app.put("/products/{id}")
def update_single_product(id: int, updated_product: ItemUpdateModel):
    with sqlite3.connect("tutorial.db") as con:
        # con.row_factory = sqlite3.Row
        cursor = con.cursor()
        cursor.execute(f"""UPDATE Products
        SET name = '{updated_product.name}', price = {updated_product.price}, quantity_in_stock = {updated_product.quantity_in_stock}
        WHERE id = {id};""")
        # cursor.rowcount atitinka, kiek eilučių buvo paveikta
        if cursor.rowcount == 0:
            raise HTTPException(
                status_code=404, detail="Product was not found")
        else:
            return {"message": "Product was successfully updated :)"}


@app.delete("/products/{id}", status_code=204)
def delete_single_product(id: int):
    with sqlite3.connect("tutorial.db") as con:
        # con.row_factory = sqlite3.Row
        cursor = con.cursor()
        cursor.execute(f"""DELETE from Products
        WHERE id = {id};""")
        # cursor.rowcount atitinka, kiek eilučių buvo paveikta
        if cursor.rowcount == 0:
            raise HTTPException(
                status_code=404, detail="Product was not found")
        else:
            return {"message": "Product was successfully deleted :)"}


@app.get("/json")
def ifgkhudjsanfpjkhgsdfgjsdjhfgsdjfba():
    return {"name": "Petras", "email": "petras@jonaitis.lt", "age": 27}


@app.get("/number-of-files-in-system")
def ifgkhudjsanfpjkhgsdfajsdjhfgsdjfba():
    return 4
