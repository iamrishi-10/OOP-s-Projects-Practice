# 1️⃣ Base Class: Vehicle
class Vehicle:
    def __init__(self, brand, model, year, rental_rate):
        self.brand = brand
        self.model = model
        self.year = year
        self.__rental_rate = rental_rate   # private

    def get_rate(self):
        return self.__rental_rate

    def set_rate(self, amount):
        if amount < 0:
            return "Error: rental rate cannot be negative"
        self.__rental_rate = amount
        return f"Rental rate updated to ₹{self.__rental_rate}/day"

    def info(self):
        return (f"Brand: {self.brand}, Model: {self.model}, "
                f"Year: {self.year}, Rate: ₹{self.__rental_rate}/day")


# 2️⃣ Car Class (inherits Vehicle)
class Car(Vehicle):
    def __init__(self, brand, model, year, rental_rate, seats):
        super().__init__(brand, model, year, rental_rate)
        self.seats = seats

    def info(self):
        return (f"Brand: {self.brand}, Model: {self.model}, "
                f"Year: {self.year}, Seats: {self.seats}, "
                f"Rate: ₹{self.get_rate()}/day")


# 3️⃣ Bike Class (inherits Vehicle)
class Bike(Vehicle):
    def __init__(self, brand, model, year, rental_rate, cc):
        super().__init__(brand, model, year, rental_rate)
        self.cc = cc

    def info(self):
        return (f"Brand: {self.brand}, Model: {self.model}, "
                f"Year: {self.year}, Engine: {self.cc}cc, "
                f"Rate: ₹{self.get_rate()}/day")


# 4️⃣ Customer Class
class Customer:
    def __init__(self, name, license_id):
        self.name = name
        self.license_id = license_id

    def info(self):
        return f"Name: {self.name}, License ID: {self.license_id}"


# 5️⃣ Rental Class
class Rental:
    def __init__(self, customer, vehicle, days):
        self.customer = customer      # Customer object
        self.vehicle = vehicle        # Vehicle (Car or Bike)
        self.days = days

    def calculate_bill(self):
        return self.days * self.vehicle.get_rate()

    def rental_summary(self):
        vehicle_type = type(self.vehicle).__name__   # "Car" or "Bike"
        total_bill = self.calculate_bill()

        summary = []
        summary.append(f"Customer: {self.customer.name}")
        summary.append(f"Vehicle: {self.vehicle.brand} {self.vehicle.model} ({vehicle_type})")
        summary.append(f"Days: {self.days}")
        summary.append(f"Total Bill: ₹{total_bill}")
        return "\n".join(summary)


# 6️⃣ Polymorphism Demo: multiple Cars and Bikes
car1 = Car("Honda", "City", 2022, 2500, 5)
car2 = Car("Toyota", "Innova", 2021, 3500, 7)

bike1 = Bike("Yamaha", "R15", 2023, 1200, 155)
bike2 = Bike("Royal Enfield", "Classic 350", 2020, 1500, 350)

vehicles = [car1, car2, bike1, bike2]

print("🔹 Vehicle Info (Polymorphism Demo)")
for v in vehicles:
    print(v.info())
print()


# 7️⃣ Final Flow

# Create a customer
customer1 = Customer("Rishi", "MH14-2020-XYZ")

# Choose a vehicle to rent (e.g., Honda City car1)
rental1 = Rental(customer1, car1, days=5)

print("🧾 Rental Summary")
print(rental1.rental_summary())
