from common import Node, print_node, take_input

head=take_input()
print_node(head)
print('\n\n')

def delete_at_head(head):
    if head is None:
        return None
    new_head=head.next
    return new_head

def delete_at_tail(head):
    if head is None or head.next is None: # Returns from empty list or list with single node
        return None
    temp=head 
    while temp.next.next is not None:     # stops at second last node, This is the standard pattern for deleting the last node in a singly ll
        temp=temp.next
    temp.next=None
    return head 

def delete_at_tail_recursively(head):
    if head is None or head.next is None:
        return None
    head.next=delete_at_tail_recursively(head.next)
    return head

def delete_at_index(head, index):
    if head is None:
        print("Nothing to delete")
        return None
    if index==0:
        return head.next 
    temp=head
    count=0
    while temp is not None and count<index-1:
        temp=temp.next
        count+=1 
    if temp is None or temp.next is None:
        print("Index out of range")
        return head 
    temp.next=temp.next.next 
    return head 

def delete_at_index_using_recursion(index, head, data):
    if head is None:
        print("Index out of bound")
        return None 
    if index==0:
        return head.next 
    head.next=delete_at_index_using_recursion(head.next, index-1, data)
    return head 

def delete_node_by_value(value, head):
    if head is None:
        return None 
    if head.data==value:
        return head.next 
    temp=head
    while temp.next is not None and temp.next.data is not value:
        temp=temp.next
    if temp.next is None:
        print("Value not present in the Linked List")
        return head
    temp.next=temp.next.next 
    return head 
    

head=delete_at_head(head) 
print('\n')
print_node(head)     
print('\n')
head=delete_at_tail(head)
print_node(head) 