def greet_user():
    print("Hello!")
greet_user()

def greet_user(username):
    print(f"Hello, {username.title()}!")
greet_user('jesse')

import pizza

pizza.make_pizza(10,"param1","param2","param3")