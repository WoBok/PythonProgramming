## 操作列表
for magician in magicians:  
&emsp;print(f"{magician.title()}, that was a great trick!")  

for value in range(1, 5):  
&emsp;print(value)  

numbers = list(range(1, 6))  
even_numbers = list(range(2, 11, 2))#设置步长  
两个星号（**）表示乘方运算  

digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]  
min(digits)  
max(digits)  
sum(digits)  

squares = [value**2 for value in range(1,11)]  

players = ['charles', 'martina', 'michael', 'florence', 'eli']  
print(players[1:4])  
print(players[:4])#从头开始  
print(players[2:])#直至末尾  
print(players[-3:])#最后三个  

for player in players[:3]:#遍历前三个
&emsp;print(player.title())

my_foods = ['pizza', 'falafel', 'carrot cake']  
friend_foods = my_foods[:]#使用切片复制列表  

dimensions = (200, 50)#创建元组，元组的值不可变  
dimensions = (400, 100)#但可以给表示元组的变量重新赋值  

