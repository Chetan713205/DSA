from common import Node, create_ll_from_list, print_node

head=create_ll_from_list([1,2,3,4,5])
print_node(head)


def search_by_value(head, value): 
    temp=head 
    count=0 
    while temp is not None: 
        if temp.data==value:
            return count 
        temp=temp.next 
        count+=1 
    return "Not found"

def search_by_recursion(head, value):
    if head is None:
        return "Not found"
    if head.data==value:
        return 0 
    return search_by_recursion(head.next, value)+1 

def search_by_index(head, index):
    temp=head
    count=0
    while temp is not None:
        if count==index:
            return temp.data 
        temp=temp.next
        count+=1
    return "Not found" 

print('\n')
print(search_by_index(head, 2))