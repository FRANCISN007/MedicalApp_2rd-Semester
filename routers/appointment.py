from fastapi import APIRouter, HTTPException
from Schemas.doctor_schema import doctors, Doctor
from Schemas.patient_schema import patients, Patient
from datetime import date
from typing import Dict
from Schemas.appointment_schema import Appointment, appointments

appointments: dict[int, Appointment] ={}
doctors: Dict[int, Doctor] ={}
patients: Dict[int, Patient] ={}
appointments_counter=1

appointment_router = APIRouter()


@appointment_router.post("/")
async def Create_appointment(patient_name: str, doctor_name: str, date: date):
    

    #doctor_name ==  Doctor.name
    #doctor = next((doc for doc in doctors if doc.name == doctor_name), None)
    doctor = next((doc for doc in doctors.values() if doc.name == doctor_name), None)
    #if doctor is None:
    if doctor is None:
        raise HTTPException(status_code=404, detail=f"Doctor {doctor_name} not found")
    #return

# Check if the time slot is available
    if any(date == date for appt in appointments):
        raise HTTPException(status_code=400, detail=f"Appointment slot at {date} is already booked")

    # Book the appointment
    appointment = Appointment(patient_name=patient_name, doctor=doctor, date=date)
    appointments.append(appointment)
    return {"message": f"Appointment booked with {doctor_name} at {date}"}

@appointment_router.get("/")
async def List_appointments():
     return [{"patient_name": appt.patient_name, "doctor_name": appt.doctor.name, "time": appt.time} for appt in appointments]



    
    