from fastapi import APIRouter, HTTPException
from app.models import Disease
from app import database

router = APIRouter()

# Get all diseases
@router.get("/", response_model=list[Disease])
def get_diseases():
    return database.diseases_db

# Search disease by name
@router.get("/search", response_model=Disease)
def search_disease(name: str):
    for disease in database.diseases_db:
        if disease.name.lower() == name.lower():
            return disease
    raise HTTPException(status_code=404, detail="Disease not found")
