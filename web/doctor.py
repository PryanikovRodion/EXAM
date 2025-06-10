class Doctor:
    def __init__(self, name: str, specialty: str):
        self.name = name
        self.specialty = specialty
        self.admissions = []
        self.diagnoses = []
        self.appointments = []
    def __repr__(self):
        return f"Doctor(name={self.name}, specialty={self.specialty})"
    def addAdmission(self,admission):
        self.admissions.append(admission)
        