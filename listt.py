sales = [1200, 1500, 1000, 1800, 1600, 1400, 1100]

print(sales[2])   #Display the sales of the 3rd day

a = max(sales)  #Find the maximum and minimum sale
print("Maximum Sales", a)
b = min(sales)
print("Minimum sales", b)

average = sum(sales)/len(sales) #Calculate the average sale
print("Average Sales", average)

count = 0       #Count how many days had sales above the average
for i in sales:
    if i > average:
        count +=1
print("The number of days sales was above average", count)

sales[3] = 1750 #Update the 4th day sale to 1750
print(sales)

sales.append(1300)  #Insert a new sale value 1300 at the end of the list
print(sales)

sales.pop() #Remove the last element temporarily and store it for later use
print(sales)

del sales[1]    #Permanently delete the sale of the 2nd day without returning any value
print("After permanent deleltion", sales)

asc = sorted(sales) #Arrange the list in ascending and descending order
print(asc)

des = sorted(sales,reverse = True)
print(des)

print("Final List", des)    #Display the final list
