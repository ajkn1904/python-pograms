#Binary Search#arr = [3, 6, 7, 10, 15, 18, 20, 21]

arr = []
print(" ")
num = int(input("No of nput: "))
print(" ")

for i in range(0, num):
    x = int(input("input number:"))
    arr.append(x)
    
print(" ")
print("The array is:", arr)


value = 18
lb = 0
ub = len(arr)-1


def bnry_srch(arr, value, lb, ub):
         while lb <= ub:
    
            mid = (ub + lb)//2
    
            if arr[mid] == value:
                return mid
    
            elif arr[mid] < value:
                lb = mid + 1
    
            else:
                ub = mid - 1
    
     
         return 0

print(" ")
get_value = bnry_srch(arr, value, lb, ub)

if get_value != 0:
    print(" ")
    print("Value,", value, "is existedb at index,", get_value)
    print(" ")
else:
    print(" ")
    print("Value,", value, "is not existed")
    print(" ")
