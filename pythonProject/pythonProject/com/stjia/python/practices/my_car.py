
from car import Car
from electric_car import ElectricCar, Battery


my_new_car = Car('audi', 'a8', 2017)
print(my_new_car.get_descriptive_name())
my_new_car.odometer_reading = 30
my_new_car.read_odometer()

my_other_car = ElectricCar('tesla', 'model s', 2018)
my_other_car.get_descriptive_name()
my_other_car.battery.describe_battery()
my_other_car_battery = Battery()

