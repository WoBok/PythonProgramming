alien = {'color':'green','points':5}
print(alien['color'])
print(alien)
alien['element3']=10
print(alien)

favorite_languages = {
'jen': 'python',
'sarah': 'c',
'edward': 'rust',
'phil': 'python',
}
print(favorite_languages)
    
print("-----------------------------------------------")

user_0 = {
    'username': 'efermi',
    'first': 'enrico',
    'last': 'fermi',
    }
for key,value in user_0.items():
    print(key)
    print(value)
    print("\n")