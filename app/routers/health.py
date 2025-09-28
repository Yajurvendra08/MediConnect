from fastapi import APIRouter
from app.models import BMIRequest

router = APIRouter()

# BMI Calculator
@router.post("/bmi")
def calculate_bmi(data: BMIRequest):
    bmi = data.weight / (data.height ** 2)
    if bmi < 18.5:
        category = "Underweight"
    elif 18.5 <= bmi < 24.9:
        category = "Normal weight"
    elif 25 <= bmi < 29.9:
        category = "Overweight"
    else:
        category = "Obesity"

    return {"bmi": round(bmi, 2), "category": category}
