## 类
__init__()是一个特殊方法Python 都会自动运行它在这个方法的定义中，形参 self 必不可少，而且必须位于其他形参的前面
当Python 调用这个方法来创建实例时，将自动传入实参 self
每个与实例相关联的方法调用都会自动传递实参 self，该实参是一个指向实例本身的引用，让实例能够访问类中的属性和方法

#定义类
class Dog:
&emsp;def __init__(self, name, age):
&emsp;&emsp;self.name = name
&emsp;&emsp;self.age = age
&emsp;def sit(self):
&emsp;&emsp;print(f"{self.name} is now sitting.")
&emsp;def roll_voer(self):
&emsp;&emsp;print(f"{self.name} rolled voer.")

#实例化
my_dog = Dog('Willie', 6)
print(my_dog.name)
m_dog.sit()

def __init__(self, make, model, year):
&emsp;self.make = make
&emsp;self.model = model
&emsp;self.year = year
&emsp;**self.odometer_reading = 0** #初始化时创建的属性

my_new_car.odometer_reading = 23

### 继承
class ElectricCar(Car):
&emsp;def __init__(self, make, model, year):
&emsp;&emsp;super().__init__(make, model, year) #初始化父类的属性
&emsp;&emsp;self.battery_size = 40 #自身特有的属性

#super() 是一个特殊的函数，让你能够调用父类的方法

#子类中重写时只需要定义与父类相同方法名称的方法即可

#组合
class Battery:
...
class Car:
&emsp;def __init__(self, make, model, year):
&emsp;&emsp;super().__init__(make, model, year)
&emsp;&emsp;self.battery = Battery() #将另一个类的实例作为类的属性

#从模块中导入类，一个模块中可存储多个类
from car import Car, ElectricCar

#导入整个模块
import car
my_mustang = car.Car('ford', 'mustang', 2024)#使用点号访问需要的类

#导入模块中的所有类
from module_name import *

#可在一个模块中导入另一个模块

#导入类时使用别名
from electric_car import ElectricCar as EC

