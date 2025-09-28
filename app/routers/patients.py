from fastapi import APIRouter, HTTPException
from app.models import Patient
from app import database

router = APIRouter()

# Create patient
@router.post("/", response_model=Patient)
def create_patient(patient: Patient):
    patient.id = len(database.patients_db) + 1
    database.patients_db.append(patient)
    return patient

# Get all patients
@router.get("/", response_model=list[Patient])
def get_patients():
    return database.patients_db

# Get patient by ID
@router.get("/{patient_id}", response_model=Patient)
def get_patient(patient_id: int):
    for patient in database.patients_db:
        if patient.id == patient_id:
            return patient
    raise HTTPException(status_code=404, detail="Patient not found")

# Update patient
@router.put("/{patient_id}", response_model=Patient)
def update_patient(patient_id: int, updated_patient: Patient):
    for index, patient in enumerate(database.patients_db):
        if patient.id == patient_id:
            updated_patient.id = patient_id
            database.patients_db[index] = updated_patient
            return updated_patient
    raise HTTPException(status_code=404, detail="Patient not found")

# Delete patient
@router.delete("/{patient_id}")
def delete_patient(patient_id: int):
    for index, patient in enumerate(database.patients_db):
        if patient.id == patient_id:
            database.patients_db.pop(index)
            return {"message": "Patient deleted"}
    raise HTTPException(status_code=404, detail="Patient not found")
