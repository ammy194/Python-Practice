# This code takes an input from the user to print a specified number of elements from a predefined list.
x = int(input("How many numbers do you want to print? "))
List = [2,4,5,6,8,12,30,43,39,54,67,89,90,100]
List1 = [2,4,5,6,8,12,30,43,39,54,67,89,90,100]
List2 = [2,4,5,6,8,12,30,43,39,54,67,89,90,100]
def even_Ammy(y):
    even_numbers = []
    for num in y:
        if num % 2 == 0:
            even_numbers.append(num)
    print("Even numbers in the list:", even_numbers)

def odd_Ammy(y):
    odd_numbers = []
    for num in y:
        if num % 2 != 0:
            odd_numbers.append(num)
    print("Odd numbers in the list:", odd_numbers)


for i in range(x):
    if i < len(List):
        print(List[i]) 
    else:
        print("INVALID INPUT GIVEN")

#This code checks the length of the list              
print("The length of the list is : ", len(List))


# This code filters the list based on whether the user wants even or odd numbers
choice = input("Do you want to print even or odd numbers? (even/odd): ")

if choice.lower() == "even":
    even_Ammy(List1)

elif choice.lower() == "odd":
    odd_Ammy(List2)

