class Car:
    # 一次模拟汽车的简单尝试
    def __init__(self, make, model, year):
        # 初始化汽车属性
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        # 返回描述性名称
        long_name = str(self.year) + '产的' + self.make + '：' + self.model
        return long_name.title()

    def read_odometer(self):
        # 返回里程数
        print("this car has " + str(self.odometer_reading) + " miles on it")

    def update_odometer(self, mileage):
        """将历程表读数设置为指定的值
            拒绝将里程数往回拨"""
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("you can't roll back an odometer!")

    def increment_odometer(self, miles):
        # 将里程表读数增加指定量
        self.odometer_reading += miles
