from pydantic import BaseModel


patients={}

class Patient(BaseModel):
    name: str
    age: int
    sex: str
    weight_Kg: str
    height_Meter: str
    phone: str

class PatientsCreateEdit(BaseModel):
    name: str
    age: int
    sex: str
    weight_Kg: str
    height_Meter: str
    phone: str


  
