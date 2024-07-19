from pydantic import BaseModel
from typing import Union

doctors={}

class Doctor(BaseModel):
    name: str
    specialization:str
    phone: str
    is_available: Union[bool, None] = None

class DoctorsCreateEdit(BaseModel):
    name: str
    specialization: str
    phone: str
    is_available: Union[bool, None] = None
      
    
