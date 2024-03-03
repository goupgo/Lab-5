def q1():
    class Vehicle:
        def __init__(self, name, max_speed, mileage):
            self.name = name
            self.max_speed = max_speed
            self.mileage = mileage
            
    class Bus(Vehicle):
        pass
    
    volvo = Bus('School Volvo', 180, 12)
    print(f'Vehical Name: {volvo.name}', f'Speed: {volvo.max_speed}', f'Mileage: {volvo.mileage}')

def q2():
    class Vehicle:
        def __init__(self, name, max_speed, mileage):
            self.name = name
            self.max_speed = max_speed
            self.mileage = mileage
            
        def seating_capacity(self, capacity):
            return f'The seating capacity of a {self.name} is {capacity} passengers'
    
    class Bus(Vehicle):
        def seating_capacity(self, capacity = 50):
            return super().seating_capacity(capacity)
            
    
    volvo = Bus('School Volvo', 180, 12)
    volvo_cap = volvo.seating_capacity()
    print(volvo_cap)
