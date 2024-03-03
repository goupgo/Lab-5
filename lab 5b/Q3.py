def q1():
    class Vehicle:
        def __init__(self, name, max_speed, mileage):
            self.name = name
            self.max_speed = max_speed
            self.mileage = mileage
            
    class Bus(Vehicle):
        def __init__(self, name, max_speed, mileage, color = "White"):
            super().__init__(name, max_speed, mileage)
            self.color = color
    
    class Car(Vehicle):
        def __init__(self, name, max_speed, mileage, color = "White"):
            super().__init__(name, max_speed, mileage)
            self.color = color
    
    volvo = Bus('Schoo Volvo', 180, 12)
    audi_q5 = Car('Audi Q5', 240, 18)
    print(f'{volvo.color} {volvo.name} Speed: {volvo.max_speed} Mileage: {volvo.mileage}')
    print(f'{audi_q5.color} {audi_q5.name} Speed: {audi_q5.max_speed} Mileage: {audi_q5.mileage}')
    
def q2():
    class Vehicle:
        def __init__(self, name, mileage, capacity):
            self.name = name
            self.mileage = mileage
            self.capacity = capacity
        
        def fare(self):
            return self.capacity * 100
    
    class Bus(Vehicle):
        def fare(self):
            fare_parent = super().fare()
            total_fare = fare_parent + fare_parent * 10 / 100
            return total_fare
        
    volvo = Bus('ssfdd', 12, 50)
    print(f'Total Bus fare is: {volvo.fare()}')    