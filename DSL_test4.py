'''Test 4:

1.	Create a max heap using python. (10th week).
2.	Also insert and delete a node in this tree.
'''

class MaxHeap: 
    def __init__(self): 
        self.heap=[]
        
    def get_parent(self, i): 
        return int((i-1)/2)

    def get_leftchild(self, i):
        return 2 * i + 1

    def get_rightchild(self, i):
        return 2 * i + 2

    def has_parent(self, i):
        return self.get_parent(i)>=0

    def has_leftchild(self,i):
        return self.get_leftchild(i) < len(self.heap)

    def has_rightchild(self,i):
        return self.get_rightchild(i) < len(self.heap)


    def swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]
  
  
  
    def insert_node(self, key):
        self.heap.append(key)
        self.heapify_up(len(self.heap)-1)
    		
    def heapify_up(self, i):
        size = len(self.heap)
        while (self.has_parent(i) and self.heap[i] > self.heap[self.get_parent(i)]):
            self.swap(i,self.get_parent(i))
            i = self.get_parent(i)

    def print_heap(self):
        print(self.heap)
    
    
    
    def delete_root(self):
        if len(self.heap)==0:
            return -1
        last_index = len(self.heap)-1
        self.swap(0,last_index)
        root = self.heap.pop()
        self.heapify_down(0)
        return root

    def heapify_down(self,i):
        while(self.has_leftchild(i)) :
            max_index = self.max_child(i)
            if max_index == -1:
                break
            if(self.heap[i] < self.heap[max_index]):
                self.swap(i,max_index)
                i = max_index
            else:
                break
        
    def max_child(self,i):
        if(self.has_leftchild(i)):
            leftc = self.get_leftchild(i)
            if(self.has_rightchild(i)):
                rightc = self.get_rightchild(i)
                if(self.heap[leftc] > self.heap[rightc]):
                    return leftc
                else:
                    return rightc
            else:
                return leftc
        else:
            return -1
 
 
        
max_heap = MaxHeap()

max_heap.insert_node(5)
max_heap.insert_node(17)
max_heap.insert_node(18)
max_heap.insert_node(3)
max_heap.insert_node(50)
max_heap.insert_node(19)
max_heap.insert_node(24)
  
    
print("\n\nThe Max Heap is: ")
'''
	 50
	/  \
   18	24
  / \	/  \
 3  5  17	19
 
'''
max_heap.print_heap()


print("\nAfter Inserting a node '20' in the max heap tree:")
'''
		 50
		/  \
	  20	24
	 / \	/ \
	18  5  17  19
	/
   3
 
'''
max_heap.insert_node(20)
max_heap.print_heap()


print("\n After delete the root node from the heap, the new heap is:")
'''
 	 24
	/  \
   20	19
  / \	/  \
 18  5  17  3
 

'''
max_heap.delete_root()
max_heap.print_heap()