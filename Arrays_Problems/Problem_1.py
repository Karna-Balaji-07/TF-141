# program to find the sum of elements in the given array

# Method 1
arr = [1,2,3,4,5,6]
add = 0
for i in range(len(arr)):
    add += arr[i]

print(f'Sum of the array is : {add}')


# method 2
# Time complexity is O(n)

arr = [1,2,3,4,5,6,7]
a = sum(arr)
print(f'sum is {a}')
