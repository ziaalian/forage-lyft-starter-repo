from battery import battery

class SpindlerBattery(battery):
     def __init__(self, last_service_date, current_date):
        super().__init__(last_service_date, current_date)