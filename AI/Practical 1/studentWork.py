# 1
number = -1
positive = number >= 0
negative = number < 0
Zero = number == 0
print("Is the number positive?", positive)
print("Is the number negative?", negative)          
print("Is the number zero?", Zero)

# 2
c = input("Enter temperature in Celsius: ")
c = float(c)
f = (c * 9/5) + 32
print("Celsius to Fahrenheit:", f)

# 3
numbers = [1,20,35,40,55,68,72,85,90,100]
print("Maximum:", max(numbers))
print("Minimum:", min(numbers))

# 4
numbers = [1,2,5,7,9,4,5,2,1]

# 5
numbers = [1, 2, 2, 3, 2, 4, 5]
element = 2

count = numbers.count(element)
print("No of occurrences of the element:", count)

# 6
marks = [75, 80, 90, 85, 70]

average = sum(marks) / len(marks)
print("Average marks:", average)