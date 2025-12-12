n = int(input("Enter the number of terms you want to print:"))
list = [0,1]
for i in range(2,n):
    new_num = list[i-1]+list[i-2]
    list.append(new_num)

print("Fibonacci is :",list)