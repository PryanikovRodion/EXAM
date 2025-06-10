from doctor import Doctor
from patient import Patient
from admission import Admission
from models import CreateDoctor, LoginDoctor, CreatePatient, LoginPatient, SetAdmission
hospital = {"doctors": {}, "patients": {}, "admissions": {}, "diagnoses": {}, "appointments": {}}

def show_hospital():
    return {"doctors":hospital["doctors"],"patients":hospital["patients"]}

def add_doctor(doctor_info: CreateDoctor):
    for doctor_id, doctor in hospital["doctors"].items():
        if doctor.name == doctor_info.name:
            return {"message": "Doctor reg failed"}
    doctor_id = len(hospital["doctors"])
    hospital["doctors"][doctor_id] = Doctor(**doctor_info.dict())
    return {"message": "Doctor added successfully", "doctor_id": doctor_id}

def login_doctor(login_info: LoginDoctor):
    for doctor_id, doctor in hospital["doctors"].items():
        if doctor.name == login_info.name:
            return {"message": "Doctor login successful", "doctor_id": doctor_id}
    return {"message": "Doctor not found or incorrect credentials"}

def add_patient(patient_info: CreatePatient):
    for patient_id, patient in hospital["patients"].items():
        if patient.name == patient_info.name:
            return {"message": "Patient reg failed"}
    patient_id = len(hospital["patients"])
    hospital["patients"][patient_id] = Patient(**patient_info.dict())
    return {"message": "Patient added successfully", "patient_id": patient_id}

def login_patient(patient_info: LoginPatient):
    for patient_id, patient in hospital["patients"].items():
        if patient.name == patient_info.name:
            return {"message": "Patient login successful", "patient_id": patient_id}
    return {"message": "Patient not found or incorrect credentials"}

def add_admission(admission_info:SetAdmission):
    doctor = hospital["doctors"].get(admission_info.doctor_id)
    patient = hospital["patients"].get(admission_info.patient_id)
    time = admission_info.time
    description = admission_info.description
    if doctor and patient:
        admission = Admission(doctor=doctor,patient=patient,time=time,description=description)
        doctor.addAdmission(admission)
        patient.addAdmission(admission)
        admission_id = len(hospital["admissions"])
        hospital["admissions"][admission_id] = admission
