## 字典
alien_0 = {'color': 'green', 'points': 5}  
alien['element3']=10  

alien_0 = {}  
alien['element1'] = 1  
alien['element2'] = 2  

alien['element2'] = 2 #修改数值  

del alien['points']

point_value = alien.get('points', 'No point value assigned.') #为防止获取不存在的键值，可使用get，其第一个参数用于指定键，第二个参数用于键不存在时返回默认值（可选参数）  

for key,value in alien.items(): #key,vaule可符合语法情况下任意命名  
&emsp;print(key)  
&emsp;print(value)  

for key in alien.keys():  
等同于
for key in alien: #在遍历字典时，会默认遍历所有的键

for name in sorted(alien.keys()): #遍历前先排序  

for value in alien.values():  

for language in set(alien.values()): #集合中的每个元素都必须是独一无二的,通过将包含重复元素的列表传入 set()，可让 Python 找出列表中独一无二的元素，并使用这些元素来创建一个集合  

## 集合
languages = {'python', 'rust', 'python', 'c'}
集合和字典很容易混淆，因为它们都是用一对花括号定义的。当花括号内没有键值对时，定义的很可能是集合。不同于列表和字典，集合不会以特定的顺序存储元素。

## 字典嵌套
可在列表中嵌套字典，在字典中嵌套列表、字典
#在列表中嵌套字典
alien_0 = {'color': 'green', 'points': 5}  
alien_1 = {'color': 'yellow', 'points': 10}  
alien_2 = {'color': 'red', 'points': 15}  
aliens = [alien_0, alien_1, alien_2]  
#在字典中嵌套列表  
pizza = {  
'crust': 'thick',  
'toppings': ['mushrooms', 'extra cheese'],  
}  
#在字典中嵌套字典
users = {  
'aeinstein': {  
'first': 'albert',  
'last': 'einstein',  
'location': 'princeton',  
},  
'mcurie': {  
'first': 'marie',  
'last': 'curie',  
'location': 'paris',  
},  
}  

