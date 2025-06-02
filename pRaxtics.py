# with open("Practicx.txt" , "w") as f:
#     f.write("Hi everyone \n We are learning python\n")
#     f.write("Using java. \nI like programming in python")




with open("Practicx.txt" , "r") as f:
    data = f.read()

new_data = data.replace("Python" , "Java")
print(new_data)


with open("Practicx.txt" , "w") as f:
    f.write(new_data)