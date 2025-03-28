class CarCompany:
    def __init__(self, name, country):
        self.name = name
        self.country = country
        self.models = []

    def add_model(self, model):
        self.models.append(model)

    def get_info(self):
        print(f'Company > {self.name}, Country > {self.country}')
        print("Models available >>> ")
        for model in self.models:
            print(f'{model.name} ({model.fuel_type})') #we will create a carmodel class

class CarModel:
    def __init__(self, name: str, price:int, fuel_type:str):
        self.name = name
        self.price = price
        self.fuel_type = fuel_type

    def get_info(self):
        print(f"Model > {self.name} | price > {self.price} | Fuel > {self.fuel_type}")

# now for EVs we create a sub Class

class ElectricCar(CarModel):
    def __init__(self, name, price, battery):
        super().__init__(name, price, fuel_type="Electric")
        self.battery = battery
    
    def get_info(self):
        super().get_info()
        print(f"Battery > {self.battery} kWh")