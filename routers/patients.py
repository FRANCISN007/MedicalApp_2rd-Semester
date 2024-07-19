from fastapi import APIRouter, HTTPException
from Schemas.patient_schema import patients, PatientsCreateEdit, Patient
from services.patient_service import PatientService

patient_router = APIRouter()


@patient_router.get("/")
async def get_all_patient():
    return patients



@patient_router.get('/{patient_id}', status_code=200)
def get_patient_by_id(patient_id: int):
    data = PatientService.get_patient_by_id(patient_id)
    return {'message': 'successful', "patient_id": patient_id,'data': data} 

    
@patient_router.post("/")
async def create_Patient_Profile(pat: Patient):
    pat_id = len(patients) + 1
    patients[pat_id] = pat.model_dump()
    return {"message":"Patient Profile Created Successfully","pat_id": pat_id, **pat.model_dump()}

   
@patient_router.put("/{patient_id}")
async def update_patient_Profile(patient_id: int, pat: Patient):
    if patient_id not in patients:
        raise HTTPException(status_code=404, detail="Patient-id not found")
    patients[patient_id].update(pat.model_dump())
    return {"message": "Patient updated successfully", "patient_id": patient_id, **pat.model_dump()}
     
          
@patient_router.delete('/{patient_id}')
def delete_patient(patient_id: int):
    PatientService.delete_patient(patient_id)
    return {'messge': 'Patient Profile deleted successfully.'}