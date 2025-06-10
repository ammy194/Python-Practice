List = [2, 4, 5, 6, 8, 12, 30, 43, 39, 54, 67, 89, 90, 100]

def prime_Ammy(y):
    prime_numbers = []
    composite_numbers = []
    for num in y:
        if num > 1:
            for i in range(2, num):
                if num % i == 0:
                    composite_numbers.append(num)
                    break  # important to stop checking once it's composite
            else:
                prime_numbers.append(num)
    
    # Print once, after all checking is done
    print("The prime numbers are:", prime_numbers)
    print("The composite numbers are:", composite_numbers)

prime_Ammy(List)
