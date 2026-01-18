class Node:
    def __init__(self, data):
        self.data=data
        self.next=None

def print_node(head):
    temp=head 
    while temp!=None:
        print(head.data)
        head=head.next
    return head 

def take_input():
    value=int(input("Enter the value of the node: "))
    head=None
    tail=None 
    while value!=-1:
        new_data=Node(value)
        if head==None:
            head=new_data
            tail=new_data
        else:
            tail.next=new_data 
            tail=new_data 
        value=int(input("Enter the value of the node: "))
    return head 

def print_length(head):
    count=0
    while head is not None:
        head=head.next
        count+=1
    return count 

def insert_at_head(head, data):
    new_node=Node(data)
    if head==None:
        return new_node
    new_node.next=head
    head=new_node 
    return head 

def insert_at_tail(head, data):
    new_node=Node(data)
    temp=head
    if temp==None:
        return new_node
    while temp.next!=None:
        temp=temp.next
    temp.next=new_node 
    return head 
    
def insert_at_index(index, data, head):
    new_data=Node(data)
    temp=head 
    count=0
    while temp is not None and count < index-1:
        temp=temp.next 
        count+=1
    new_data.next=temp.next
    temp.next=new_data
    return head 


        
new_head=take_input()
print_node(new_head)
print('\n')
print(print_length(new_head))
new_head=insert_at_head(new_head, 2000)
print('\n')
print_node(new_head)
print('\n')
new_head=insert_at_tail(new_head, 2000)
print_node(new_head)
print('\n')
new_head=insert_in_middle(588, 2, new_head)
print_node(new_head)