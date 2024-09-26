## 列表
motorcycles = ['honda', 'yamaha', 'suzuki']  
motorcycles[2] = "ikuzus"  
motorcycles.append("ahamay")  

motorcycles = []  
motorcycles.append('honda')  
motorcycles.insert(0, 'ducati')  
del motorcycles[0]  
popped_motorcycle = motorcycles.pop()#接收弹出的值  
first_owned = motorcycles.pop(1)  
motorcycles.remove('ducati')  

cars = ['bmw', 'audi', 'toyota', 'subaru']  
cars.sort(reverse=True)  
print(sorted(cars))#临时排序  
cars.reverse()#反转元素  
len(cars)  
每当需要访问最后一个列表元素时，都可以使用索引 -1，仅当列表为空时，这种访问最后一个元素的方式才会导致错误  
