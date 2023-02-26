from abc import ABC, abstractmethod
from car_factory import CarFactory


class Car(CarFactory):
    def __init__(self, last_service_date):
        self.last_service_date = last_service_date

    @abstractmethod
    def needs_service(self):
        return True
