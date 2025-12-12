
# num1 = 1
# num2 = 0
# sum = num1 + num2
# print("The sum of {0} and {1} is {2}".format(num1,num2,sum))

# import math
# r = float(input("Enter the radius of the circle: "))
# area = math.pi * r * r 
# print(area)

# x = int(input("Enter first number:"))
# y = int(input("Enter second number:"))
# temp = y
# y = x
# x = temp
# print("the numbers after swapping are:/n")
# print("First number:",x)
# print("Second number:",y)

# X = int(input("Enter first number:"))
# y = int(input("Enter second number: "))
# X,y = y,X
# print("X=",X)
# print("Y",y)

# ch = input("Enter a character:")
# ascii_value = ord(ch)
# print("The ascii value of ",ch,"is ",ascii_value)

# print("Enter a string")
# text = input()
# print("Enter a word to remove")
# word = input()
# text = text.replace(word,"")
# print(text)

# E = {0,2,4,6,8,10,12}
# N = {1,2,3,4,5}
# print("Union of E&N",E|N)
# print("Intersection of E&N",E&N)
# print("Difference of E and N",E-N)
# print("Symmetric set difference of E and N",E^N)

# import calendar
# YEAR = int(input("Enter the year: "))
# MONTH = int(input("Enter the month: "))
# print(calendar.month(YEAR,MONTH))

# Program to check if a number is a perfect number

num = int(input("Enter a number: "))

sum_of_divisors = 0

for i in range(1, num):
    if num % i == 0:
        sum_of_divisors += i

if sum_of_divisors == num:
    print(num, "is a Perfect Number")
else:
    print(num, "is not a Perfect Number")
