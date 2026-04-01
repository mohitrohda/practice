from pydantic import BaseModel

class Address(BaseModel):
    city : str
    state: str
    pin: int

class Patient(BaseModel):

    name : str
    age : int
    gender: str
    address : Address

address_dict = {'city':'bangluru',
                    'state': 'Tamil Nadu',
                    'pin': 490000}
    
address1 = Address(**address_dict)

patient_dict = {'name': 'mohit',
                    'gender': 'male',
                    'age': 21,
                    'address':address1}
    
patient1 = Patient(**patient_dict)

print(patient1)
print(patient1.name)
print(patient1.address.city)
print(patient1.address.pin)