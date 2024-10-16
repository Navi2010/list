lists = [12, 45, 32, 67, 79]
print('the original list: ', lists)

sum = 0
for list in lists:
    sum = sum + list

average = sum/len(lists)

print('the sum of the list is: ', sum)
print('the average of the list is: ', average)

lists.sort()
print('the min number in this list is: ', lists[0])
print('the max number in this list is: ', lists[-1])