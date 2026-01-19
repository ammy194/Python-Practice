# (a) Create list
sales = [120, 150, 130, 170, 160, 140, 110]
print("Sales List:", sales)

# (b) Maximum and Minimum
print("Maximum Sale:", max(sales))
print("Minimum Sale:", min(sales))

# (c) Average sale
average = sum(sales) / len(sales)
print("Average Sale:", average)

# (d) Function to count even values
def count_even(lst):
    count = 0
    for x in lst:
        if x % 2 == 0:
            count += 1
    return count

print("Even Sales Count:", count_even(sales))

# (e) Remove user entered value
value = 150
sales.remove(value)
print("After removing", value, ":", sales)

# (f) Pop last element temporarily
temp = sales.pop()
print("Popped value:", temp)
print("After pop:", sales)

# (g) Delete value at index
del sales[2]
print("After deleting index 2:", sales)

# (h) Add new sale
sales.append(180)
print("After appending new value:", sales)

# (i) Frequency of elements
freq = {}
for x in sales:
    freq[x] = freq.get(x, 0) + 1
print("Frequency:", freq)

# (j) Second largest & second smallest
unique = list(set(sales))
unique.sort()
print("Second Smallest:", unique[1])
print("Second Largest:", unique[-2])

# (k) Merge two sorted lists without sort()
list2 = [100, 125, 190]
merged = []
i = j = 0

while i < len(sales) and j < len(list2):
    if sales[i] < list2[j]:
        merged.append(sales[i])
        i += 1
    else:
        merged.append(list2[j])
        j += 1

merged.extend(sales[i:])
merged.extend(list2[j:])

print("Merged List:", merged)
