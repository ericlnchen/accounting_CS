
class Liability:
    def __init__(self, value, date, isCurrent):
        self.value = value
        self.date = date
        self.isCurrent = isCurrent

class accountsPayable(Liability):
    def __init__(self, value, date, isCurrent):
        super().__init__(value, date, isCurrent)