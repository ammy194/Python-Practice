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

def prime_Ammy(y):
    prime_numbers = []
    for num in y:
        if num > 1:
            # for i in range(2, int((num)**0.5) + 1):
            for i in range(2, num - 1):
                if (num % i) == 0:
                    break
            else:
                prime_numbers.append(num)
    print("Prime numbers in the list:", prime_numbers)







# This code filters the list based on whether the user wants even or odd numbers
choice = input("Do you want to print even or odd numbers? \n (even/odd/prime): ")
match choice.lower():
    case "even":
        even_Ammy(List1)
    case "odd":
        odd_Ammy(List2)
    case "prime":
        prime_Ammy(List2)
    case _:
        print("Invalid choice. Please enter 'even' or 'odd'.")


