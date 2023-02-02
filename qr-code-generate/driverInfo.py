import json

class DriverInfo:
    def __init__(self, firstname, lastname, licence_num, address, dob):
        self.firstname = firstname
        self.lastname = lastname
        self.licence_num = licence_num
        self.address = address
        self.dob = dob

    @property
    def name(self):
        return f'{self.firstname} {self.lastname}'

    @property
    def infoBehindQR(self):
        # create a dict of important values
        driverCard = {
            "Full name":self.firstname + self.lastname,
            "licence_num": self.licence_num,
            "Address": self.address,
            "Date of Birth": self.dob
        }

        return json.dumps(driverCard)