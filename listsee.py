temps = (32, 35, 30, 28, 33, 31, 29)


print(temps[2]) #(a)
print("The maximum temperature is : ", max(temps))  #maximum temperature
print("The minimum temperature is : ", min(temps))  #minimum temperature

average = sum(temps)/len(temps)
print("The average temperature is: ", average)
count = 0
for t in temps:
    if t>average:
        print("Days above average:", t)


#converting into list and change 4th day to 34

temp_list = list(temps)
temp_list[3] = 34
print(temp_list)  #updated list

temp_list.append(36)
temps = tuple(temp_list)    #converting into tuple
print(temps)

#arrange in ascending order
temps1 = tuple(sorted(temps))
print("Ascending order: ", temps1)

#arrange in descending order
temps2 = tuple(sorted(temps, reverse = True))
print("Descending order: ",temps2)

#Displaying final result

print("Final tuple: ", temps2)