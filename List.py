# a = int(input("How many numbers do you want to print? "))
List = [2,4,5,6,8,12,30,43,39,54,67,89,90,100]
for i in range(len(List)):
    if i < len(List):
        print(List[i])
    else:
        print("INVALID INPUT GIVEN")
               
print("The length of the list is : ", len(List))

for i in List:
    if(i % 2 == 0):
        print("The even numbers are : ", i)
    else:
        print("The odd numbers are : ", i)
