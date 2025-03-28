from database import CarDatabase
from car_classes import CarCompany, CarModel, ElectricCar

def run_commands():
    db = CarDatabase()

    # Creating Companies
    rollsroyce = CarCompany("Rolls Royce", "Germany")

    # Adding Cars to Companies

    rollsroyce.add_model(CarModel('Ghost', 70000000, "Petrol"))

    # Adding Companies to Database
    db.add_company(rollsroyce)

    while True:
        print("\nCar Management System")
        print("1. Display all cars")
        print("2. Search for a car")
        print("3. Exit")

        choice = input("Enter your choice: ")
        if choice == "1":
            db.display_all_cars()
        elif choice == "2":
            name = input("Enter model name: ")
            car = db.find_car(name)
            if car:
                car.display_info()
            else:
                print("Car not found!")
        elif choice == "3":
            break
        else:
            print("Invalid choice, try again.")
