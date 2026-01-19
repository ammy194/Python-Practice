rain = (12, 15, 10, 8, 14, 11, 9)

print(rain[4])      #Display the rainfall recorded on the 5th day.

print("Minimum Sales", min(rain))   #minimum sales
print("Maximum Sales", max(rain))  #maximum sales

average = sum(rain)/len(rain)
print("Average rainfall:",average)

count = 0
for i in rain:
    if i> average:
        count +=1
print("Number of days with rainfall above average : ", count)


temp_rain = list(rain)
print("The tuple is converted into a list: ", temp_rain)

temp_rain[2] = 13
print(temp_rain) #converted 3rd element to 13

a = temp_rain.append(16)
print("List version: ", temp_rain)

final_tuple = tuple(temp_rain)
print("Tuple version: ", final_tuple)

final_tuple = tuple(sorted(final_tuple))
print("Ascending Order", final_tuple)

final_tuple = tuple(sorted(final_tuple, reverse = True))
print("Descending Order", final_tuple)