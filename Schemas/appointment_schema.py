from pydantic import BaseModel
from datetime import date
from Schemas.doctor_schema import doctors, Doctor
from Schemas.patient_schema import patients, Patient


appointments={} 

class Appointment(BaseModel):
    patient: Patient
    doctor: Doctor
    date: date

   
    


