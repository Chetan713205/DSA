from common import *

head_of_even=create_ll_from_list([1, 2, 3, 4, 5, 6])
head_of_odd=create_ll_from_list([1, 2, 3, 4, 5])

print_node(head_of_even)
print('\n')
print_node(head_of_odd)
print('\n')

def middle_of_ll(head):
    if head is None or head.next is None:
        return head 
    length=length_of_ll(head) 
    middle=length//2 
    temp=head
    count=0 
    while count<middle: 
        temp=temp.next
        count+=1
    return temp

## P1 speed = x
## P2 speed = 2x
## Then when P2 reach to end then P1 will be at middle ---------> 2 Pointer Approach
def middle_of_ll_using_slow_and_fast(head):
    if head is None or head.next is None:
        return head 
    slow=head
    fast=head 
    while fast is not None and fast.next is not None: 
        fast=fast.next.next 
        slow=slow.next 
    return slow 

head_odd_mid=middle_of_ll_using_slow_and_fast(head_of_odd)
head_even_mid=middle_of_ll_using_slow_and_fast(head_of_even)

print(head_odd_mid.data)
print('\n')
print(head_even_mid.data)