# class Person:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age

# p = Person("Amartya",18)
# print(p.name,p.age)

# class Animal:
#     def speak(self):
#         return "Some sound"

# class Dog(Animal):  # Dog inherits from Animal
#     def speak(self):  # override
#         return "Bark"

# d = Dog()
# print(d.speak())  # Bark


# class Animal:
#     def speak(self):
#         return "Some Sound"
# class Dog(Animal):
#     def speak (self):
#         return "bark"
        

# class A:
#     def __init__(self):          # default constructor
#         self.x = 0

# class B:
#     def __init__(self, x):      # parameterized constructor
#         self.x = x

# a = A()
# b = B(10)
# print(a.x, b.x)  # 0 10

# class Sample:
#     def __init__(self):
#         self.public = "I am public"
#         self.__private = "I am private"

# s = Sample()
# print(s.public)         # OK
# # print(s.__private)    # AttributeError
# # Access private via name-mangled form (not recommended)
# print(s._Sample__private)  # I am private   


# class Sample:
#     def __init__(self):
#         self.public = "I am public"
#         self.__private = "I am private"
# s = Sample()
# print(s.public)



# write_student.py
# students = [
#     {"id": 1, "name": "Amartya", "marks": 85},
#     {"id": 2, "name": "Riya", "marks": 72},
# ]

# # Write to file (text, CSV-like)
# with open("students.txt", "w") as f:
#     for s in students:
#         f.write(f"{s['id']},{s['name']},{s['marks']}\n")

# # Read and display
# with open("students.txt", "r") as f:
#     for line in f:
#         sid, name, marks = line.strip().split(",")
#         print(f"ID: {sid}, Name: {name}, Marks: {marks}")



# write new file
# with open("data.txt", "w") as f:
#     f.write("Hello\n")

# # append to file
# with open("data.txt", "a") as f:
#     f.write("More\n")

# # read file
# with open("data.txt", "r") as f:
#     print(f.read())




# import numpy as np
# py_list = [10,20,30,40]
# arr = np.array(py_list)
# mean_value = arr.mean()
# print(mean_value)


# import pandas as pd

# data = {
#     "Roll": [1,2,3,4],
#     "Name": ["Amartya","Riya","Karan","Maya"],
#     "Maths": [80, 35, 60, 45],
#     "Physics": [75, 40, 50, 42],
#     "Chemistry": [90, 38, 55, 48]
# }
# df = pd.DataFrame(data)

# Percentage (simple average of three subjects)
# df["Percentage"] = df[["Maths","Physics","Chemistry"]].mean(axis=1)

# # i. Status
# df["Status"] = df["Percentage"].apply(lambda p: "Pass" if p >= 40 else "Fail")

# # ii. Average marks in each subject
# subject_averages = df[["Maths","Physics","Chemistry"]].mean()

# # iii. Top 3 students by Percentage
# top3 = df.sort_values("Percentage", ascending=False).head(3)

# print(df)
# print("\nSubject averages:\n", subject_averages)
# print("\nTop 3 by percentage:\n", top3[["Roll","Name","Percentage"]])


import numpy as np

# 1-D array from list
l1 = [1,2,3,4]
a1 = np.array(l1)
print("1D:", a1, "shape:", a1.shape)

# 2-D array from nested lists
l2 = [[1,2,3],[4,5,6]]
a2 = np.array(l2)
print("2D:\n", a2, "shape:", a2.shape)
