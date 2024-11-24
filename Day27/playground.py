#add as many numbers as we want
def add(*args):
    sum = 0
    for num in args:
        sum += num
    
    return sum

#test add
sum = add(1,76,5,3,8)
print(sum)

# **kwargs test
def calculate(**kwargs):
    print(kwargs)
    
calculate(f=3, multiply=12)

# class test
class Car:
    
    def __init__(self, **kw):
        self.make = kw.get("make")
        self.model = kw.get("model")
        
my_car = Car(make="Nissan")
print(my_car.make)