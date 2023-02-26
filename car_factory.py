class CarFactory():
    def __init__(self, current_date, last_service_date, current_mileage, last_service_mileage):
        self.current_date = current_date
        self.last_service_date = last_service_date
        self.current_mileage = current_mileage
        self.last_service_mileage = last_service_mileage

    def create_calliope(self):
        return self.current_date, self.last_service_date, self.current_mileage, self.last_service_mileage
    
    def create_glissade(self):
        return self.current_date, self.last_service_date, self.current_mileage, self.last_service_mileage

    def create_palindrome(self):
        return self.current_date, self.last_service_date, self.current_mileage, self.last_service_mileage

    def create_rorschach(self):
        return self.current_date, self.last_service_date, self.current_mileage, self.last_service_mileage

    def create_thovex(self):
        return self.current_date, self.last_service_date, self.current_mileage, self.last_service_mileage


        





        

    

    
