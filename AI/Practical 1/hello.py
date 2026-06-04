#1
width = 10
height = 5
area = width * height
print("Area of the rectangle:", area)

#2
number1 = 15
number2 = 200
swap_variable = number1

print("Before swapping: number1 =", number1, ", number2 =", number2)
number1 = number2
number2 = swap_variable
print("After swapping: number1 =", number1, ", number2 =", number2)

#3
text = "This is a python text file"
print(text[0])
print(text[len(text)//2])
print(text[-1])

#4
name = """Shelomi
Nipunika"""
print(name)

#5
number1 = 10
number2 = 5

print("sum:", number1 + number2)
print("difference:", number1 - number2)
print("product:", number1 * number2)
print("division:", number1 / number2)

#6
c = 25
f = (c * 9/5) + 32
print("Celsius to Fahrenheit:", f)

#7
length = 7
print("area:", length * length)
print("perimeter:", 4 * length)

#8
text = "University"
print("First character: ",text[0])
print("Last character: ",text[-1])
print("Length of the string: ",len(text))

#9
text = "Learning Python Programming"
print(text[9:15])

#10
full_name = "Shelomi Nipunika De Alwis"
parts = full_name.split()
initials = parts[0][0] + parts[1][0] + parts[2][0] + parts[3][0]
print("Initials:", initials)

#11
number1 = 5
number2 = 10

number1, number2 = number2, number1

print("number1 =", number1)
print("number2 =", number2)

#12
number = 1_000_000_000
print(number)

#13
text = "Python"
# text[0] = 'J'     
# print(text) this will give an error because strings are immutable
new_text = 'J' + text[1:]
print(new_text)

#14
text = """Name: Shelomi
Degree: Bachelor of Information and Communication Technology
University: University of Ruhuna"""
print(text)

#15
length = 10
volume = length ** 3
print("Volume of the cube:", volume)

#16
text = "Hello World"
count = len(text.replace(" ", ""))
print("Number of characters:", count)

#17
text = "Python Programming"
print(text[::2])

#18
nic = "123456789214"
print("length of NIC:", len(nic)) 

#19
text1 = "Python"
text2 = "Programming"
print(text1 + " " + text2)