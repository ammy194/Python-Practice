# # class student:
# #     name = "Karan"
# # s1 = student()
# # print(s1.name)

# # s2 = student()
# # print(s2.name)


# class Car:
#     name = "Honda"
#     color = "blue"

# car1 = Car()
# print(car1.name)


class Student:

    def __init__(self,name,marks):
        self.name = name
        self.marks = marks
        print("adding new student to database..")

s1 = Student("karan",97)
print(s1.name, s1.marks)


s2 = Student("Amartya",100)
print(s2.name,s2.marks)
