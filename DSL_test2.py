'''Test 2:

1.	Create queue using list. Also insert and delete a value from queue. (8th week).
'''

queue = []
x=int(input("No of Inputs: "))
for i in range(0,x):
    value=int(input("Input: "))
    queue.append(value)
 
print('\n\nThe Queue is: ',queue)

queue.append("Anika")
print('\nThe new Queue is: ',queue)

print("\nDeleted item: ",queue.pop(0))
print('\nQueue after elements are popped:',queue,"\n\n")