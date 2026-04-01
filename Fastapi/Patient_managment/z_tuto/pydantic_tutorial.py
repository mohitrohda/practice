from pydantic import BaseModel, EmailStr, AnyUrl, Field
from typing import List, Dict, Optional, Annotated

class Patient(BaseModel):

    name: Annotated[str, Field(max_length=25, title = 'Name of the patient', description = 'name must be under 25 characters', example=['mohit','rohit'])]         #str = Field(max_length = 25)
    age: int
    weight : Annotated[float, Field(gt=  0, lt = 130, strict=True)]
    married : Annotated[bool, Field(default=None, description = 'patient is married or not')]
    allergies : Annotated[Optional[List[str]], Field(max_length = 5, default=None) ]
    contact_details : Dict[str, str]
    email: EmailStr
    linkdin_url : AnyUrl


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


patient_info = {'name': 'Mohit', 'age': 21, 'weight': 65,  'allergies': ['dust', 'mud'], 'email':'abc@gmail.com',
                'linkdin_url': 'https://www.linkedin.com/in/mohit-rohda/' ,'contact_details': {'ph. no': '1234567890'}}

patient1 = Patient(**patient_info)


insert_patient_data(patient1)