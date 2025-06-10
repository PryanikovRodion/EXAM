from fastapi import FastAPI
from models import LoginDoctor, CreateDoctor, CreatePatient, LoginPatient, SetAdmission
from hospital_core import hospital, login_doctor, add_doctor, show_hospital, login_patient, add_patient
app = FastAPI()

@app.get("/show_hospital")
def showHospital():
    return show_hospital()

@app.post("/login_doctor")
def loginDoctor(data: LoginDoctor):
    return login_doctor(data)

@app.post("/reg_doctor")
def regDoctor(data: CreateDoctor):
    return add_doctor(data)

@app.post("/login_patient")
def loginPatient(data: LoginPatient):
    return login_patient(data)

@app.post("/reg_patient")
def regPatient(data: CreatePatient):
    return add_patient(data)

@app.post("/patient/new_admissions")
def createAdmission(admission_info:SetAdmission):
