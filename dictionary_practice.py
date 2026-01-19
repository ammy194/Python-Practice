students = {"Ravi": 82, "Asha": 91, "John": 76}
print(students)
#Add new and update marks

students["Neha"] = 98
students["Amartya"] = 100
students["Ravi"] = 10
print ("Updated: ", students)

#Display key-value pairs
for name,marks in students.items():
    print(name, ":", marks)

topper = max(students, key = students.get)
print("TOpper: ", topper)

#above 75
for name,marks in students.items():
    if marks> 75:
        print(name)

#frequency 

para = "Python is easy to use and is powerful"
words = para.split()
freq = {}

for w in words:
    if w in freq:
        freq[w] = freq[w]+1
    else:
        freq[w] = 1

print("Frequency: ", freq)

#merge dictionary with addition

d1 = {"a": 10, "b": 20}
d2 = {"b": 5, "c": 30}

for key in d2:
    if key in d1:
        d1[key]+=d2[key]
    else:
        d1[key] = d2[key]
print("Merged dictionary:", d1)

#create dicitonary from 2 list

keys = ["x", "y", "z"]
values = [1,2,3]
new_dict = dict(zip(keys,values))
print("New dictionary:",new_dict)

#invert dicitonary

inverted = {v:k for k,v in new_dict.items()}
print("Inverted dictionary:",inverted)

#error demonstration
try:
    test = {[1,2,3]: "value"}
except TypeError as e:
    print("Error:",e)

