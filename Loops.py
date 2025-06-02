i = [1,2,3,4,5,6,7]
i = 1
while i<= 15:
    if(i % 2 == 0):
        i += 1
        continue
    print(i)
    i += 1


    i = 1
while i <= 5:
    print(i)
    if(i == 3):
        break
    i += 1


    nums = [1,4,9,16,25,36,49,64,81,100]

    x = 49
    idx = 0
    while idx < len(nums):
        if(nums[idx == x]):
            print("FOUND", idx)
            break
        else:
            print("FINDING....")
        idx += 1
