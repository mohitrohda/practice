from pydantic import BaseModel, EmailStr, AnyUrl, Field, field_validator
from typing import List, Dict, Optional, Annotated

class Patient(BaseModel):

    name: str
    age: int
    weight : float
    married : Optional[bool] = None
    allergies : List[str]
    contact_details : Dict[str, str]
    email: EmailStr
    linkdin_url : AnyUrl

    @field_validator('name')
    @classmethod
    def transform_name(cls, value):
        return value.upper()

    @field_validator('email')
    @classmethod
    def email_validator(cls, value):

        valid_domains = ['hdfc.com', 'sbi.com']
        domain_name= value.split('@')[-1]

        if domain_name not in valid_domains:
            raise ValueError('Not a valid domain')
        
        return value
    
    @field_validator('age', mode = 'after')
    @classmethod
    def validate_age(cls, value):
        if 0 < value < 120:
            return value
        else:
            return ValueError('Age should be in range 0 to 100')


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


patient_info = {'name': 'Mohit', 'age': '21', 'weight': 65,  'allergies': ['dust', 'mud'], 'email':'abc@sbi.com',
                'linkdin_url': 'https://www.linkedin.com/in/mohit-rohda/' ,'contact_details': {'ph. no': '1234567890'}}

patient1 = Patient(**patient_info)


insert_patient_data(patient1)