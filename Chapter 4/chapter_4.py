magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(f"{magician.title()}, that was a great trick!")
    print(f"I can't wait to see your next trick, {magician.title()}")
    print("\n")
print("Thank you, everyone. That was a great magic show!")
print("-------------------------------------------------")
squares = []
for value in range(1,11):
    squares.append(value)
print(squares)
squares = [value**2 for value in range(1,11)]
print(squares)
print("-------------------------------------------------")
odds = [value for value in range(1,21,2)]
for odd in odds:
    print(odd)
cubes = [value**3 for value in range(1,11)]
for cube in cubes:
    print(cube)
