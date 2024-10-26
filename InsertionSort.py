arr = [5,2,9,1,7, 0,4,2,1,8,23,45,34]

for i in range(1, len(arr)):
    current = arr[i]
    j = i-1
    while j >=0 and arr[j] < current:
        arr[j+1] = arr[j]
        j = j-1
    arr[j+1] = current

print(arr)
 
            