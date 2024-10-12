from car import Car

class CarManager:
    
    CAR_CREATE_ITERATION = 8
    CAR_DELETION_MARKER = -360
    CAR_BASE_SPEED = 3
    
    cars = []
    car_speed = CAR_BASE_SPEED
    
    def __init__(self):
        ''' constructor'''
        self.create_car()
    
    def create_car(self):
        ''' create a new car'''
        car = Car(self.car_speed)
        self.cars.append(car)
        
    def move_cars(self):
        ''' move all cars. Remove those out of bounds'''
        temp_cars = self.cars
        for car in self.cars:
            car.move()
            
            if car.xcor() < self.CAR_DELETION_MARKER:
                temp_cars.remove(car)
            
        self.cars = temp_cars
        
    def increase_speed(self):
        '''increases speed on all cars'''
        self.car_speed += self.CAR_BASE_SPEED
        for car in self.cars:
            car.set_speed(self.car_speed)
            
    def check_collision(self, frogger):
        ''' Check if collision has happened'''
        for car in self.cars:
            if(frogger.distance(car) < 20):
                return True
            
        return False