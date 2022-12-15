alan_2022_results = [5,4,3,9,8,7,6,6,6,6,6,6,6,7,7,8,9,9,9,15,10,14,13,12,11]

#total = 0
#for num in alan_2022_results:
#    total += num

#avg = total / len(alan_2022_results)
#print(total, avg)

def average(nums):
    total = 0
    for num in nums:
        total += num
    return total/len(nums)


min = alan_2022_results[0]
for num in alan_2022_results:
    if num < min:
        min = num
print(min)

