from fastapi import HTTPException
from Schemas.patient_schema import patients


class PatientService:

   
   
   @staticmethod
   def get_patient_by_id(patient_id):
        patient = patients.get(patient_id)
        if not patient:
            raise HTTPException(detail='Patient not found.', status_code=404)
        return patient
   
   

   @staticmethod
   def delete_patient(patient_id: int):
        patient = patients.get(patient_id)
        if not patient:
            raise HTTPException(detail='Patient not found.', status_code=404)
        del patients[patient_id]       
