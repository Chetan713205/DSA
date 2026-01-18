class Node:
    def __init__(self, data):
        self.data=data
        self.next=None
        
l1=Node(10)
l2=Node(20)
l3=Node(30)
l4=Node(40)

l1.next=l2
l2.next=l3
l3.next=l4
l4.next=None

head=l1
# def print_node(head):
#     while head!=None:
#         print(head.data, end=" -> ")
#         head=head.next

# print_node(head)

def print_node(head):
    temp=head
    while temp!=None:
        print(temp.data, end=" -> ")
        temp=temp.next
    
    print('\n')
    temp=head
    while temp!=None:
        print(temp.data, end=" -> ")
        temp=temp.next

print_node(head)