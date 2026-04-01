from pydantic import BaseModel, EmailStr, AnyUrl, computed_field
from typing import List, Dict

class Patient(BaseModel):

    name: str
    age: int
    weight : float
    height : float #meter
    married : bool = 'false'
    allergies : List[str]
    contact_details : Dict[str, str]
    email: EmailStr
    linkdin_url : AnyUrl

    @computed_field
    @property
    def bmi(self) -> float:
        bmi = round(self.weight/(self.height**2),2)
        return bmi


def insert_patient_data(patient : Patient):

    print(patient.name)
    print(patient.age)
    print(patient.weight)
    print(patient.married)
    print(patient.allergies)
    print(patient.contact_details)
    print(patient.email)
    print(patient.linkdin_url)
    print('bmi', patient.bmi)
    print("Success")




patient_info = {'name': 'Mohit', 'age': 70, 'weight': 65, 'height': 1.2,  'allergies': ['dust', 'mud'], 'email':'abc@gmail.com',
                'linkdin_url': 'https://www.linkedin.com/in/mohit-rohda/' ,'contact_details': {'ph. no': '1234567890', 'emergency':'1234567890'}}

patient1 = Patient(**patient_info)


insert_patient_data(patient1)