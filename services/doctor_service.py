from fastapi import HTTPException
from Schemas.doctor_schema import doctors, doctors


class DoctorService:
   
   
    @staticmethod
    def get_doctor_by_id(doctor_id):
        doctor = doctors.get(doctor_id)
        if not doctor:
            raise HTTPException(detail='Doctor not found.', status_code=404)
        return doctor
   

   

    @staticmethod
    def delete_doctor(doctor_id: int):
        doctor = doctors.get(doctor_id)
        if not doctor:
            raise HTTPException(detail='Doctor not found.', status_code=404)
        del doctors[doctor_id]       





