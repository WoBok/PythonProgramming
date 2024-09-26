## If
if car == "bmw":  
&emsp;print(car.upper())  
else:  
&emsp;print(car.title())  
if-elif-else  
Python 并不要求 if-elif 结构后面必须有 else 代码块。  

age_0 >= 21 **and** age_1 >= 21  
age_0 >= 21 **or** age_1 >= 21  

requested_toppings = ['mushrooms', 'onions', 'pineapple']  
'mushrooms' **in** requested_toppings  
user **not in** banned_users  

requested_toppings = []  
if requested_toppings:#判断非空  
&emsp;for requested_topping in requested_toppings:  
&emsp;&emsp;print(f"Adding {requested_topping}.")  
&emsp;print("\nFinished making your pizza!")  
else:  
&emsp;print("Are you sure you want a plain pizza?")  