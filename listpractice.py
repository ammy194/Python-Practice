sales = [120, 150, 130, 170, 160, 140, 110]
print("Sales:", sales)

print("Maximum sales: ", max(sales))
print("Minimum sales: ", min(sales))

average = sum(sales)/len(sales)
print("Average:", average)

def count_even(lst):
    count = 0
    for x in lst:
        if x%2 ==0:
            count+=1
    return count

print("Even sales count: ", count_even(sales))

value = 150
sales.remove(value)
print("After removing",value, "The final sales are:", sales)

temp = sales.pop()
print("Popped Value: ", temp)
print("After pop: ", sales)

sales.append(180)
print("Sales after appending: ",sales)

freq = {}
for x in sales:
    if x in freq:
        freq[x] = freq[x]+1
    else:
        freq[x] = 1
        
print("Frequency: ",freq)


unique = list(set(sales))
#set removes any duplicates
unique.sort()
print("Second Smallest: ", unique[1])
print("Second Largest: ", unique[-1])

# (k) Merge two sorted lists without sort()




