from fastapi import FastAPI
from app.routers import patients, diseases

app = FastAPI(
    title="MediConnect API",
    description="A simple medical API for patients, diseases, and health calculators.",
    version="1.0.0"
)

# Include routers
app.include_router(patients.router, prefix="/patients", tags=["Patients"])
app.include_router(diseases.router, prefix="/diseases", tags=["Diseases"])


@app.get("/")
def root():
    return {"message": "Welcome to MediConnect API - FastAPI Medical Project"}
