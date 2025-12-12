students = {
    "S1": {"Name": "Ravi",  "Age": 17, "Marks": 85}, 
    "S2": {"Name": "Neha",  "Age": 18, "Marks": 92}, 
    
    "S3": {"Name": "Karan", "Age": 17, "Marks": 78}
}

for sid , details in students.items():
    print("Student ID",sid)

    for keys,values,in details.items():
        print(keys,':', values,':',)

print()






