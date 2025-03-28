class CarDatabase : 
    def __init__(self):
        self.car_companies = []

    def add_company(self, company):
        self.car_companies.append(company)

    def find_car(self, model_name):
        for company in self.car_companies:
            for model in company.models:
                if model.name.lower() == model_name.lower():
                    return model
                
        return None
    
    def display_all_cars(self):
        for company in self.car_companies:
            company.get_info()