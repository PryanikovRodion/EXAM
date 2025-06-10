class Admission:
    def  __init__(self,patient,doctor,time,description):
        self.patient = patient
        self.doctor = doctor
        self.time = time
        self.description = description
    def __repr__(self):
        return f"doctor:{self.doctor.name},patient:{self.patient.name},time:{self.time},description:{self.description}"
