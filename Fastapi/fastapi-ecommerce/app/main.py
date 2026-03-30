from fastapi import FastAPI, HTTPException, Query
from service.products import get_all_products

app = FastAPI()

#static route
@app.get("/")
def root():
    return {"message": "Welcome to the FastAPI."}

#dynamic route
#@app.get('/products/{id}')
#def get_products(id:int):
#    products = ['Brush', 'Laptop', 'Mouse', 'Monitor']
#    return products[id] 

# @app.get("/products")
# def get_products():
#     return get_all_products()


@app.get("/products")
def list_products(
    name: str = Query(
        default = None,
        min_length = 1, 
        max_length = 50, 
        description = "Search by product name (case insensitive)"
    )
):
    return name