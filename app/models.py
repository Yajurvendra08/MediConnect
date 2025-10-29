from pydantic import BaseModel
from typing import Optional

# Patient model
class Patient(BaseModel):
    id: Optional[int] = None
    name: str
    age: int
    symptoms: str

# Disease model
class Disease(BaseModel):
    name: str
    symptoms: str
    treatment: str

# BMI request model
# class BMIRequest(BaseModel):
#     weight: float  # in kg
#     height: float  # in meters
