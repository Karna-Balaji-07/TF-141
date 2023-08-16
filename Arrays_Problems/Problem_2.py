# Program to find the largest element in the array


# Method_1
arr = [1,2,3,4,99,76,56,4,3257,8746,2346,754,56534,768765,435432]
max = arr[0]
for i in range(len(arr)):
    for j in range(i+1,len(arr)):
        if max < arr[j]:
            max = arr[j]

print(f'Maximum element in the array is {max}')


# Method _2
arr = [1,2,3,4,99,76,56,4,3257,8746,2346,754,56534,768765,435432]
max = arr[0]
for i in range(len(arr)):
    if max < arr[i]:
        max = arr[i]

print(f'The maximum element is {max}')
