class Patient:
    def __init__(self, name):
        self.name = name
        self.admissions = []
        self.diagnoses = []
        self.appointments = []
    
    def __repr__(self):
        return f"Patient(name={self.name})"
    
    def addAdmission(self,admission):
        self.admissions.append(admission)
