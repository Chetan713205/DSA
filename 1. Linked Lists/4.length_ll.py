from common import Node, print_node, take_input

def print_length(head):
    count=0
    temp=head
    while temp!=None:
        temp=temp.next
        count+=1
    return count

newhead=take_input()
print_node(newhead)
print(print_length(newhead))