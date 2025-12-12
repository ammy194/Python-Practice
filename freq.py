numbers = [10,20,30,40,10,20,30,12,21]
freq = {}

for n in numbers:
    if n in freq:
        freq[n]+=1

    else:
        freq[n] = 1

print("Element Frequency: ")
for key,values in freq.items():
    print(key,':',values)