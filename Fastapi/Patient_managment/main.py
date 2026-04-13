from fastapi import FastAPI, Path, HTTPException, Query
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field, computed_field
from typing import Annotated, Literal, Optional
import json

app = FastAPI()

class Patient(BaseModel):

    id: Annotated[str, Field(..., description='ID of the Patient', examples=['P001'])]
    name: Annotated[str, Field(..., description='Name of the Patient', examples=['Mohit Rohda'])]
    city: Annotated[str, Field(..., description='City where patient living')]
    age: Annotated[int, Field(..., gt=0, lt=120, description='Age of the Patient')]
    gender: Annotated[Literal['male', 'female', 'others'], Field(..., description='gender of the Patient')]
    height: Annotated[float, Field(..., gt=0, description='height of the Patient in meters')]
    weight: Annotated[float, Field(..., gt=0, description='weight of the Patient in kgs')]

    @computed_field
    @property
    def bmi(self) -> float:
        bmi = round(self.weight/(self.height**2),2)
        return bmi
    
    @computed_field
    @property
    def verdict(self) -> str:
        if self.bmi < 18.5:
            return 'UnderWeight'
        elif self.bmi < 25:
            return 'Normal'
        elif self.bmi < 30:
            return 'Normal'
        else:
            return 'Obese'
        

class PatientUpdate(BaseModel):

    name: Annotated[Optional[str], Field(default=None)]
    city: Annotated[Optional[str], Field(default=None)]
    age: Annotated[Optional[int], Field(default=None, gt=0)]
    gender: Annotated[Optional[Literal['male', 'female']], Field(default=None)]
    height: Annotated[Optional[float], Field(default=None, gt=0)]
    weight: Annotated[Optional[float], Field(default=None, gt=0)]


def load_data():
    with open ('patients.json', 'r') as f:
        data = json.load(f)
    return data

def save_data(data):
    with open ('patients.json', 'w') as f:
        data = json.dump(data, f)


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


@app.post('/create')
def create_patient(patient: Patient):
    #load existing data
    data = load_data()

    #checking patient id is already exist?
    if patient.id in data:
        raise HTTPException(status_code=400, detail='Patient ID already exist')

    #new patient add to database
    data[patient.id] = patient.model_dump(exclude='id')

    #save into json file
    save_data(data)

    return JSONResponse(status_code=201, content= {'message': 'patient created sussessfully'})


@app.put('/edit')
def update_patient(patient_id: str, patient_update: PatientUpdate):

    #load data
    data = load_data()

    #checking patirnt id is exist in database or not
    if patient_id not in data:
        raise HTTPException(status_code=404, detail= ' Patient id not exist')
    
    #extracting data of patient with patient id
    existing_patient_info = data[patient_id]

    #making dist of variable 
    updated_patient_info = patient_update.model_dump(exclude_unset=True)

    for key, value in updated_patient_info.items():
        existing_patient_info[key] = value

    existing_patient_info['id'] = patient_id
    patient_pydantic_obj = Patient(**existing_patient_info)

    existing_patient_info = patient_pydantic_obj.model_dump(exclude='id')

    #add this dist to data
    data[patient_id] = existing_patient_info

    #save data
    save_data(data)

    return JSONResponse(status_code=201, content={'message': 'Patient edit successfully'})

@app.delete('/delete/{patient_id}')
def delete_patient(patient_id: str):

    #load data
    data = load_data()

    #checking patirnt id is exist in database or not
    if patient_id not in data:
        raise HTTPException(status_code=404, detail= ' Patient id not exist')
    
    del data[patient_id]

    save_data(data)

    return JSONResponse(status_code=201, content={'message': 'Patient deleted successfully'})
