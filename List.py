# This code takes an input from the user to print a specified number of elements from a predefined list.
a = int(input("How many numbers do you want to print? "))
List = [2,4,5,6,8,12,30,43,39,54,67,89,90,100]
for i in range(a):
    if i < len(List):
        print(List[i])
    else:
        print("INVALID INPUT GIVEN")

#This code checks the length of the list              
print("The length of the list is : ", len(List))

#This code checks if the numbers in the list are even or odd.
for i in List:
    if(i % 2 == 0):
        print("The even numbers are : ", i)
    else:
        print("The odd numbers are : ", i)
