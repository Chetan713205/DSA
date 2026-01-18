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

def create_ll_from_list(l):
    head=None
    tail=None
    for i in l: 
        new_node=Node(i) 
        if head==None:
            head=new_node
            tail=new_node 
        else:
            tail.next=new_node
            tail=new_node 
    return head 

def length_of_ll(head):
    count=0
    temp=head
    while temp!=None:
        temp=temp.next
        count+=1
    return count
