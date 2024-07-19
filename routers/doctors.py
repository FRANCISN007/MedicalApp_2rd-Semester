from fastapi import APIRouter, HTTPException, Response
from Schemas.doctor_schema import doctors, DoctorsCreateEdit, Doctor
from services.doctor_service import DoctorService



doctor_router = APIRouter()


@doctor_router.get("/")
async def get_all_Doctor():
    return doctors



@doctor_router.get('/{doctor_id}', status_code=200)
def get_doctor_by_id(doctor_id: int):
    data = DoctorService.get_doctor_by_id(doctor_id)
    return {'message': 'successful', "doctor_id": doctor_id,'data': data} 



@doctor_router.post("/")
async def create_Doctor_Profile(doct: Doctor):
    doct_id = len(doctors) + 1
    doctors[doct_id] = doct.model_dump()
    return {"message":"Doctor Profile Created Successfully","doct_id": doct_id, **doct.model_dump()}


@doctor_router.put("/{doctor_id}")
async def update_Doctor_Profile(doctor_id: int, doct: Doctor):
    if doctor_id not in doctors:
        raise HTTPException(status_code=404, detail="Doctor not found")
    doctors[doctor_id].update(doct.model_dump())
    return {"message": "Doctor updated successfully", "doctor_id": doctor_id, **doct.model_dump()}



@doctor_router.delete('/{doctor_id}')
def delete_doctor(doctor_id: int):
    DoctorService.delete_doctor(doctor_id)
    return {'messge': 'Doctor account deleted successfully.'}