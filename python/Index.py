

class Index:
    def __init__(self):
        self.subunit = None
        self.userExternalID = None
        self.period = None
        self.courseID = None
        self.survey = None
        self.lastName = None
        self.firstName = None

    def get_subunit(self):
        return self.subunit

    def set_subunit(self,aStr):
        self.subunit = aStr

    def get_userEternalID(self):
        return self.userExternalID

    def set_userExternalID(self,aStr):
        self.userExternalID = aStr

    def get_period(self):
        return self.period

    def set_period(self,aStr):
        self.period = aStr
        
    def get_courseID(self):
        return self.courseID

    def set_courseID(self,aStr):
        self.courseID = aStr
        
    def get_survey(self):
        return self.survey

    def set_survey(self,aStr):
        self.survey = aStr
    
    def get_lastName(self):
        return self.lastName

    def set_lastName(self,aStr):
        self.lastName = aStr

    def get_firstName(self):
        return self.firstName

    def set_firstName(self,aStr):
        self.firstName = aStr
