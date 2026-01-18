## Examples: Packet of Bread, Pringles
## Follows LIFO (Last In First Out) principle FIFO (First In First Out) principle 
## Abstract Data Type: Is a type for object whose behaviour is defined by a set of operations 
## Operations: Top/Peek, Push, Pop, Size, IsEmpty
##--------------------------------------------------------------------------------
'''
Stack implementation: Using Inbuild Python List

'''

class StackUsingList:
    def __init__(self):
        self.__stack=[]         ## Very Important to make it private so that the functionality is not affected by inbuilt functions
    
    def push(self, data):
        self.__stack.append(data)
        print(f"Pushed {data} to the Stack")
    
    def size(self):
        return len(self.__stack)
    
    def is_empty(self):
        if len(self.__stack)==0:
            return True
        else:
            return False 
    
    def top(self):
        if self.is_empty():
            print("Stack is Empty")
            return None
        return self.__stack[-1]
    
    def pop(self):
        if self.is_empty():
            print("Stack is Empty, cannot pop")
            return None
        else:
            return self.__stack.pop()

my_stack=StackUsingList()
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