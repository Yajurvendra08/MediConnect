from app.models import Patient, Disease

# In-memory patient database
patients_db: list[Patient] = [
    Patient(id=1, name="Dev Bandi", age=45, symptoms="Asthma"),
    Patient(id=2, name="Sukha Patil", age=81, symptoms="Hypertension"),
    Patient(id=3, name="Motha Rakesh", age=76, symptoms="Diabetes"),
]

# Simple disease dataset
diseases_db: list[Disease] = [
    Disease(name="Diabetes", symptoms="Increased thirst, frequent urination, fatigue", treatment="Insulin, diet control"),
    Disease(name="Hypertension", symptoms="Headache, dizziness, chest pain", treatment="Lifestyle changes, medication"),
    Disease(name="Asthma", symptoms="Shortness of breath, wheezing, coughing", treatment="Inhalers, avoiding triggers"),
]
