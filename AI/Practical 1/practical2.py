# task 1
is_active = True 
is_admin = False 
print(type(is_active)) 
print(30 > 20) 
print(30 < 20) 

# task 2
print(bool('Hi')) 
print(bool('')) 
print(bool(100)) 
print(bool(0)) 

# task 3
import constant
print(constant.PI)
print(constant.GRAVITY)

# task 4

# This is a single-line comment 
def calculate_area(radius): 
    """Calculate area of a circle""" 
    return 3.14 * radius * radius 
print(calculate_area(7))

# print print docstring
# print(calculate_area.__doc__)

# task 5
price = input('Enter price: ') 
tax = input('Enter tax rate: ') 
net_price = float(price) * float(tax) / 100 
print('Net price:', net_price)

print('\n')

# task 6
a = 10 
b = 20 
print(a + b) 
print(a * b) 
print(a > b) 
print(a != b)

print('\n')

# task 7
price = 9.99 
print(price > 5 and price < 10) 
print(not(price > 10))

# task 8
numbers = [3, 8, 1, 6] 
print(max(numbers)) 
print(min(numbers)) 
print(sum(numbers))

# task 9
fruits = ['apple', 'banana', 'cherry'] 
print(fruits)

# task 10
letters = ['p', 'r', 'o', 'g', 'r', 'a', 'm'] 
print(letters[0]) 
print(letters[-1])

# task 11
my_list = ['p','r','o','g','r','a','m','i','n','g'] 
print(my_list[2:5]) 
print(my_list[:]) #print entire list

# task 12
odd = [1, 3, 5] 
odd.append(7) 
odd.extend([9, 11]) 
print(odd) 
del odd[1] 
print(odd)

# task 13
my_list = [3, 8, 1, 6, 8] 
print(my_list.count(8)) # counts occurrences of 8 in the list
print(my_list.index(6)) # finds the index of first occurrence of 6

# task 14
letters = ['p', 'r', 'o', 'b', 'l', 'e', 'm'] 
print('p' in letters) 
print('a' not in letters) 