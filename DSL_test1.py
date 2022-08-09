'''Test 1:
1. Take user input of list A using map (7 th week).
2. Insert and delete some values in list.'''

num = int(input("\n\n\nNumber of inputs : "))
A = list(map(int, input("Inputs: ").split()))[:num]

print("The List is: ",A)

A.insert(2,90)
print("\nNew List after inserting 90 in the 2nd index: ",A)

A.extend([23,45,65])
print("\nNew List after inserting some values using extend: ",A)

A.pop()
print("\nNew List after deleting the last element: ",A)

A.remove(23)
print("\nNew List after deleting 23: ",A)

A.pop(3)
print("\nNew List after deleting the element of 3rd index: ",A,"\n\n")