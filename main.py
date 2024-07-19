from fastapi import FastAPI
from routers.patients import patient_router
from routers.doctors import doctor_router
from routers.appointment import appointment_router


app = FastAPI()

app.include_router(patient_router, prefix ="/Patient", tags =["Patients"])
app.include_router(doctor_router, prefix ="/Doctor", tags = ["Doctors"])
app.include_router(appointment_router, prefix="/Appointment", tags= ["Appointment"])

@app.get('/home')
def index():
    return "WELCOME TO MY MEDICAL APPOINTMENT APPLICATION"

