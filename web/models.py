from pydantic import BaseModel, Field
from typing import Optional, List

class LoginDoctor(BaseModel):
    name: str = Field(..., description="Name of the doctor")

class CreateDoctor(BaseModel):
    name: str = Field(..., description="Name of the doctor")
    specialty: str = Field(..., description="Specialty of the doctor")

class CreatePatient(BaseModel):
    name: str = Field(..., description="Name of the patient")

class LoginPatient(BaseModel):
    name: str = Field(..., description="Name of the patient")

class SetAdmission(BaseModel):
    patient_id = Field(...)
    time:str = Field(..., description="Time of Admission")
    doctor_id:int = Field(...)
    description:str

