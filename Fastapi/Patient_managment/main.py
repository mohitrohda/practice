from fastapi import FastAPI, Path, HTTPException, Query
import json

app = FastAPI()

def load_data():
    with open ('patients.json', 'r') as f:
        data = json.load(f)
    return data


@app.get("/")
def hello():
    return {'message' : 'Welcome to Patient Managment System'}

@app.get("/about")
def about():
    return {"message" : "Fully Functional API to manage Patients Records"}

@app.get("/view")
def view():
    data = load_data()
    return data

@app.get("/patient/{patient_id}")
def view_patient(patient_id: str = Path(..., description = 'ID of the patient', example = 'P001' )): #we can add more condn on path like regex or arthmatics like ge, gt, le, lt
    #load all patients
    data = load_data()

    if patient_id in data:
        return data[patient_id]
    raise HTTPException(status_code = 404, detail = 'Patient Not Found') #return the error and correct status code to the client

@app.get('/sort')
def sort_patients(
sort_by : str = Query(..., description = 'Sort on the basis of height, weight, bmi'),
order : str = Query('asc', description = 'sort in Asc or Desc order')):
    
    valid_field = ['height', 'weight', 'bmi']

    if sort_by not in valid_field:
        raise HTTPException(status_code = 400, detial = f'Invalid feild select from {valid_field}')
    
    if order not in ['asc', 'desc']:
        raise HTTPException(status_code = 400, detial = f'Invalid feild select asc or desc')
    
    data = load_data()

    sort_order = True if order=='desc' else False

    sorted_data = sorted(data.values(), key = lambda x: x.get(sort_by, 0), reverse = sort_order)

    return sorted_data