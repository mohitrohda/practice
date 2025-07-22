from fastapi import FastAPI
from enum import Enum

app = FastAPI()

#first endpoint
'''@app.get("/hello")
async def hello():
    return "welcome"

@app.get("/hello/{name}")
async def hello(name):
    return f"welcome to the fastapi server {name}" '''

class AvailableCuisines(str, Enum):
    indian = 'indian'
    american = 'american'
    italian = 'italian'

food_items= {
    'indian' : [ "Samosa", "Dosa" ],
    'american' : [ "Hot Dog", "Apple Pie"],
    'italian' : [ "Ravioli", "Pizza"]
}

@app.get("/get_items/{cuisine}")
async def get_item(cuisine: AvailableCuisines):
    return food_items.get(cuisine)

'''# valid_cuisines = food_items.keys()

@app.get("/get_items/{cuisine}")
async def get_items(cuisine):
    
    if cuisine not in valid_cuisines:
        return f"Supported cuisines are {valid_cuisines}"
    
    return food_items.get(cuisine) '''