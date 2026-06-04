rgb = ('red', 'green', 'blue') 
print(rgb[0]) 
print(rgb[1]) 
print(rgb[2]) 

thistuple = ("apple", "banana", "cherry", "apple") 
print(thistuple) 
print(len(thistuple)) 

numbers = (3,) 
print(type(numbers)) 
numbers = (3) 
print(type(numbers))

tuple1 = ("abc", 34, True, 40, "male") 
print(tuple1) 
print("\n")

x = ("apple", "banana", "cherry") 
y = list(x) 
y[1] = "kiwi" 
x = tuple(y) 
print(x) 

print("\n")

thistuple = ("apple", "banana", "cherry") 
thistuple += ("orange",) 
print(thistuple) 

print("\n")

thistuple = ("apple", "banana", "cherry") 
y = list(thistuple) 
y.remove("apple") 
thistuple = tuple(y) 
print(thistuple) 

print("\n")

tuple1 = ("a", "b", "c") 
tuple2 = (1, 2, 3) 
print(tuple1 + tuple2) 

print("\n")

skills = {'Python', 'Databases', 'Software Design'} 
empty_set = set()
skills = set() 
if not skills: 
    print("Empty sets are falsy") 

print("\n")

thisset = {"apple", "banana", "cherry"} 
for x in thisset: 
    print(x) 

thisset.add("orange") 
print(thisset)
thisset.update({"mango", "papaya"}) 
print(thisset)

color_set = {'red', 'yellow', 'white'} 
color_set.remove('yellow') 
color_set.discard('white')
print(color_set)

print("\n")

A = {1, 2, 3} 
B = {3, 4, 5} 
print(A | B)   # Union 
print(A & B)   # Intersection 
print(A - B)   # Difference 
print(A ^ B)   # Symmetric Difference

print("\n")

print({1,2}.issubset({1,2,3})) 
print({1,2,3}.issuperset({1,2})) 

rainbow = ('red', 'green', 'blue') 
other = ('black', 'white') 
nested_set = set((frozenset(rainbow), frozenset(other))) 
print(nested_set)

print("\n")
person = {"name": "Jessa", "country": "USA", "age": 20} 
print(person["name"]) 
print(person.get("country"))

person["weight"] = 50 
person.update({"height": 6}) 
print(person)

for key, value in person.items(): 
    print(key, ":", value)

person.pop("age")
print(person)

person.popitem()
print(person)

address = {"city": "Houston", "state": "Texas"} 
person = {"name": "Jessa", "address": address} 
print(person['address']['city']) 