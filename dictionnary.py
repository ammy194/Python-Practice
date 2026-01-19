# (a) Create dictionary
students = {"Ravi": 82, "Asha": 91, "John": 76}
print("Students:", students)

# (b) Add new student & update marks
students["Neha"] = 88
students["Ravi"] = 85

# (c) Display key–value pairs
for name, marks in students.items():
    print(name, ":", marks)

# (d) Student with maximum marks
topper = max(students, key=students.get)
print("Topper:", topper)

# (e) Students above 75
print("Above 75:")
for name, marks in students.items():
    if marks > 75:
        print(name)

# (f) Frequency dictionary of words
para = "python is easy and python is powerful"
words = para.split()
word_freq = {}

for w in words:
    word_freq[w] = word_freq.get(w, 0) + 1

print("Word Frequency:", word_freq)

# (g) Merge dictionaries with addition
d1 = {"a": 10, "b": 20}
d2 = {"b": 5, "c": 30}

for key in d2:
    if key in d1:
        d1[key] += d2[key]
    else:
        d1[key] = d2[key]

print("Merged Dictionary:", d1)

# (h) Create dictionary from two lists
keys = ["x", "y", "z"]
values = [1, 2, 3]
new_dict = dict(zip(keys, values))
print("New Dictionary:", new_dict)

# (i) Invert dictionary
inverted = {v: k for k, v in new_dict.items()}  
print("Inverted Dictionary:", inverted) 

# (j) Error demonstration
try:
    test = {[1, 2, 3]: "value"}
except TypeError as e:
    print("Error:", e)
