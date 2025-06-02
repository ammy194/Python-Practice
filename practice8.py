list1 = ["m" , "a" , "a" , "m" , "p"]


copy_list1 = list1.copy()
copy_list1.reverse()
if(copy_list1 == list1):
    print("Palindrome")
else:
    print("NOT Palindrome")