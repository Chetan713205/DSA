class Node:
    def __init__(self, data):
        self.data=data
        self.next=None

def print_node(head):
    temp=head
    while temp!=None:
        print(temp.data, end=" -> ")
        temp=temp.next

def take_input():
    value=int(input("Enter the value of Node:- "))
    head=None
    while value!=-1:
        new_node=Node(value)
        if head==None:
            head=new_node
        else:
            temp=head
            while temp.next!=None:
                temp=temp.next
            temp.next=new_node  

        value=int(input("Enter the value of Node:- "))
    return head   

newhead=take_input()
print_node(newhead)
