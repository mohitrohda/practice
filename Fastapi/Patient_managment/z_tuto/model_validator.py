from pydantic import BaseModel, EmailStr, AnyUrl, Field, model_validator
from typing import List, Dict, Optional, Annotated

class Patient(BaseModel):

    name: str
    age: int
    weight : float
    married : bool = 'false'
    allergies : List[str]
    contact_details : Dict[str, str]
    email: EmailStr
    linkdin_url : AnyUrl

    @model_validator(mode = 'after')
    def validate_emergency_contact(cls, model):
        if model.age > 60 and 'emergency' not in model.contact_details:
            raise ValueError('Patient above 60 must have emergency contacts')
        return model


def insert_patient_data(patient : Patient):

    print(patient.name)
    print(patient.age)
    print(patient.weight)
    print(patient.married)
    print(patient.allergies)
    print(patient.contact_details)
    print(patient.email)
    print(patient.linkdin_url)
    print("Success")


patient_info = {'name': 'Mohit', 'age': 70, 'weight': 65,  'allergies': ['dust', 'mud'], 'email':'abc@gmail.com',
                'linkdin_url': 'https://www.linkedin.com/in/mohit-rohda/' ,'contact_details': {'ph. no': '1234567890', 'emergency':'1234567890'}}

patient1 = Patient(**patient_info)


insert_patient_data(patient1)