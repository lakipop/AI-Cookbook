# 1
tuple1 = ("Science", "Maths", "History", "Geography","English","Art")
print("Subjects in tuple1:", tuple1)

# 2
A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8, 9}

print(A | B) 
print(A & B)   
print(A - B)   
print(A ^ B)

# 3
student = {
    "name": "Sashini",
    "age": 22,
    "height": 160, 
    "country": "Sri Lanka"
}

print("Student details:")
print(student)

student["weight"] = 55 # Adding new key-value pair
print(student)

student.pop("country") # Removing country key-value pair
print("Updated student details:")
print(student)

# 4
Address = {
    "street": "123 Main St",
    "city": "Colombo",
    "zip": "10000"
}

Marks = {
    "Maths": 95,
    "Science": 90,
    "English": 85
}

student = {
    "name": "Sashini",
    "age": 22,
    "address": Address,
    "marks": Marks
}

print(student['address']['city'])
print(student['marks']['Science'])

# 5
fruits = ("apple", "banana", "cherry", "avacado", "strawberry")
list_fruits = list(fruits)
list_fruits[1] = "pomegranate"
fruits = tuple(list_fruits)
print(fruits)

# 6
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)

joined_tuple = tuple1 + tuple2
print("Joined tuple:", joined_tuple)

# 7
fruits = {"apple", "banana", "cherry"}
print("Original set:", fruits)
fruits.update({"orange", "kiwi", "mango"})
print("Updated set:", fruits)

# 8
tuple = ("Python", 42, 3.14, True)
print(len(tuple))

# 9
fruits = ("apple", "banana", "cherry", "orange")
for item in range(len(fruits)):
    print(fruits[item])

# 10
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}
print(A | B)   # Union 
print(A & B)   # Intersection 
print(A - B)   # Difference 
print(A ^ B)   # Symmetric Difference

# 11
fruits = {"apple", "banana", "cherry", "orange"}
element = "banana"

if element in fruits:
    print(f"{element} exists in the set.")
else:
    print(f"{element} does not exist in the set.")

# 12
A = {1, 2, 3}
B = {1, 2, 3, 4, 5}

if A.issubset(B):
    print("A is a subset of B")
else:
    print("A is not a subset of B")

# 13
X = {1, 2, 3}
Y = {4, 5, 6}

if X.isdisjoint(Y):
    print("X and Y are disjoint sets")
else:
    print("X and Y are not disjoint")

# 14
rainbow = ('red', 'green', 'blue') 
other = ('black', 'white') 
nested_set = set((frozenset(rainbow), frozenset(other)))
print(nested_set)

# 15
student = {
    "name": "Sashini",
    "age": 22,
    "address": Address,
    "marks": Marks
}
student.pop("age")

# 16
student = {"name": "Sashini", 
           "age": 22, 
           "course": "CS"}
student.clear()

print("Cleared dictionary:", student)