name = "Rahul Verma"

#First and last character

print("First character: ",name[0])
print("Second character: ",name[-1])

#Convert the string to uppercase and lowercase

print(name.upper())
print(name.lower())

#Count characters excluding spaces

count = len(name.replace(" ", ""))
print(count)

count1 = len(name) #including spaces
print(count1)

count2 = name.replace("Verma", "Sharma") #replace verma with sharma
print(count2)

if "Rahul" in name:         #To check if rahul is in name
    print("Rahul is there in name")
else:
    print("Rahul is not in name")


#Split into first and last name

first_name , last_name = name.split()   #Split into first and last name
print("First name: ", first_name)
print("Last name: ", last_name)

#Final modified string
print("Final modified string", name)
