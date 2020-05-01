

class Student():
    def __init__(self, first, last, handle, cohort):
        self.first_name = first
        self.last_name = last
        self.slack_handle = handle
        self.cohort = cohort
        
    def __repr__(self):
        return f'{self.first_name} {self.last_name} is in {self.cohort}.'