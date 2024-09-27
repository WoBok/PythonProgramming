## 函数
def greet_user():
&emsp;print("Hello!")
greet_user()

def greet_user(username):
&emsp;print(f"Hello, {username.title()}!")
greet_user('jesse')

#关键字实参
def describe_pet(animal_type, pet_name):
&emsp;print(f"\nI have a {animal_type}.")
print(f"My {animal_type}'s name is {pet_name.title()}.")
describe_pet(animal_type='hamster', pet_name='harry')

#默认值
def describe_pet(pet_name, animal_type='dog'):
describe_pet(pet_name='willie')

#返回值
 def get_formatted_name(first_name, last_name):
&emsp;full_name = f"{first_name} {last_name}"
&emsp;return full_name.title()
musician = get_formatted_name('jimi', 'hendrix')
print(musician)

#None（表示变量没有值）。可将 None 视为占位值。在条件测试中，None 相当于 False。
def build_person(first_name, last_name, age=None):

#将列表传递给函数后，函数就可以对其进行修改了，在函数中对这个列表所做的任何修改都是永久的

#每个函数都应只负责一项具体工作

#传递列表的**副本**
function_name(list_name[:])

#传递任意数量的实参  
def make_pizza(*toppings):形参名 # *toppings 中的星号让 Python 创建一个名为 toppings的元组，该元组包含函数收到的所有值
#如果要让函数接受不同类型的实参，必须在函数定义中将接纳任意数量实参的形参放在最后。
def make_pizza(size, *toppings):

#形参 **user_info 中的两个星号让Python 创建一个名为 user_info 的字典，该字典包含函数收到的其他所有名值对  
def build_profile(first, last, **user_info):  
&emsp;user_info['first_name'] = first
&emsp;user_info['last_name'] = last
&emsp;return user_info

user_profile = build_profile('albert', 'einstein',location='princeton',field='physics')  

#使用import关键字导入模块（module），模块是.py文件
e.g. import pizza

#从模块中导入特定的函数
#由于在 import语句中显式地导入了指定函数，因此在调用时只需指定其名称即可
from module_name import function_0, function_1, function_2

#给导入的函数起别名
from pizza import make_pizza as mp
#给导入的模块起别名
import pizza as p
#导入模块中的全部函数，由于导入了每个函数，可通过名称来调用每个函数，无须使用点号（dot notation）
from pizza import *

#形参换行
def function_name(
&emsp;parameter_0, parameter_1, parameter_2,
&emsp;parameter_3, parameter_4, parameter_5):
&emsp;function body...

