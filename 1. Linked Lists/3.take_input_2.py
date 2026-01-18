class Node:
    def __init__(self, data):
        self.data=data
        self.next=None

def print_node(head):
    temp=head
    while temp!=None:
        print(temp.data, end=" -> ")
        temp=temp.next                      # reads the existing link without altering node contents, preserving the original chain for reuse

def take_input():
    value=int(input("Enter the value of Node:- "))
    head=None
    tail=None
    while value!=-1:
        new_node=Node(value)
        if head==None:
            head=new_node
            tail=new_node
        else:
            tail.next=new_node
            tail=new_node

        value=int(input("Enter the value of Node:- "))
    return head 

newhead=take_input()
print_node(newhead)


"""
| Step | Input | Action                            | head/tail State  | List Chain                    |
| ---- | ----- | --------------------------------- | ---------------- | ----------------------------- |
| 1    | 10    | head=tail=Node(10)                | head→10, tail→10 | 10 → None                     |
| 2    | 20    | tail.next=Node(20), tail=Node(20) | head→10, tail→20 | 10 → 20 → None                |
| 3    | 30    | tail.next=Node(30), tail=Node(30) | head→10, tail→30 | 10 → 20 → 30 → None           |
"""