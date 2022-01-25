class Car():
    def __init__(self):
        self.model="BEN"
    def change_model(self):
        self.model="CAR"
    def change_model_another(self):
        self.model="TRUCK"
car=Car()
car.change_model_another()
car.change_model()
print(car.model)