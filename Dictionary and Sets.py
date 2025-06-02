#info = {
 #   "key" : "value",
  ## "learning" : "coding",
    ##Topics" : ("dict", "sets"),
    #"age": 35,
    #"is_adult":True,
    #"marks": 94.4


#}

#info["name"] = "Amartya"
#print(info)


student = {
    "Name" : "Amartya",
    "Subject" : {
        "Physics" : 97,
        "Chemistry" : 98,
        "Math" : 87

    }
}

chicken = {"city" : "delohi"}
student.update(chicken)
print(student["Subject"]["Chemistry"])
print(student["Name"])
print(list(student.keys()))
print(len(student))
print(student.values()) 

