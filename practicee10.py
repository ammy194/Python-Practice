nums = [1,4,9,16,25,36,49,64,81,100]
x = 49

idx  = 0
for el in nums:
    if(el == 49):
        print("DONE",idx)
        break
    idx += 1





nums = [1,2,3,4,5,5,6,7,8,9,10]
for el in nums:
    print(el)    #el is a random variable


Nonveg = ["Chicken Lollipop - Rs 210" , "Crispy chicken - Rs 450" , "Chilli Chicken - Rs 218" , "Chicken Manchow Soup - Rs 345"]
for value in Nonveg:
    print(value)   #value is a random variable


Letter = "Amartya"
for char in Letter:
    print(char)
    if(char == "r"):
        print("r FOUND")
        continue
else:
    print("END")
    