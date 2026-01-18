## in order to reach O(1) complexity we will be inserting or deleting from the head of the Linked List 
##

class Node:
    def __init__(self, data):
        self.data=data 
        self.next=None 

class StackUsingLinkedLists:
    def __init__(self):
        self.head=None 
        self.count=0 

    def push(self, data):
        new_node=Node(data)
        self.count+=1
        if self.head is None:
            self.head=new_node
            return f"Inserted {data} in the Stack"
        new_node.next=self.head        # Linking the new node with the head  
        self.head=new_node 
        return f"Inserted {data} in the Stack" 

    def top(self):
        if self.head is None:
            return None 
        return self.head.data 

    def pop(self):
        if self.head is None:
            print(f"Stack is empty, cannot pop element")
        popped_data=self.head.data
        self.head=self.head.next 
        self.count-=1 
        return popped_data
    
    def size(self):
        return self.count
    
    def is_empty(self):
        return self.count==0

my_stack=StackUsingLinkedLists()
print(my_stack.is_empty())
my_stack.push(10)
my_stack.push(20)
my_stack.push(30)
my_stack.push(40)
my_stack.push(50)
print(my_stack.is_empty())
print(my_stack.top())
print(my_stack.size())
print(my_stack.pop())
print(my_stack.pop())
print(my_stack.pop())
print(my_stack.pop())
print(my_stack.pop())
print(my_stack.pop())
