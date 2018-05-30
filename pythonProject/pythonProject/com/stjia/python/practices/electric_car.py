
from car import Car

class ElectricCar(Car):
    # 模拟电动车的独特之处

    def __init__(self, make, model, year):
        # 初始化父类属性
        super().__init__(make, model, year)
        self.battery = Battery()



class Battery:
    # 电池信息
    def __init__(self, battery_size=70):
        # 初始化电瓶属性
        self.battery_size = battery_size

    def describe_battery(self):
        # 打印一条电瓶描述信息
        if self.battery_size == 70 :
            range =240
        elif self.battery_size == 85:
            range = 270
        else:
            range = 'other'
        message = "this car can go approximately " + str(range) + " miles on a full charge."
        print(message)