from fastapi import FastAPI

app = FastAPI()

# @app.get("/")
# def say_hello():
#     return{"message":"hello"}

# @app.get("/greeting")
# def greeting():
#     return{"greeting": "how is you"}


products = [
    {
        "id": 1,
        "name": "Milk",
        "price": 1.99,
        "available": True
    },
    {
        "id": 2,
        "name": "Bread",
        "price": 0.99,
        "available": True
    },
    {
        "id": 3,
        "name": "Cheese",
        "price": 2.99,
        "available": False
    }
]


@app.put("/greeting/{prod_id}")
def add_product(prod_id,prod: dict):
    for product in products:
        if product["id"] == int(prod_id):
            print("Found")
            product = prod
            print(products)
            return {"message":"Update successful"}
    return {"message":"Product not found"}
