from common import *

def reverse_ll_recursively(head):
    if head is None or head.next is None:
        return head                                        ## Base Case
    small_ll_head=reverse_ll_recursively(head.next) ## Recursive Case --> this will return all the data in reverse except the first node
    temp=small_ll_head
    while temp.next is not None:
        temp=temp.next 
    temp.next=head
    head.next=None
    return small_ll_head 


## N    1 ->  2  ->  3  ->  4  ->  5  ->  None 
## p    c
## N <- 1     2  ->  3  ->  4  ->  5  ->  None  
## p    c     n 
## N <- 1 <-  2      3  ->  4  ->  5  ->  None
##      p     c      n 
## N <- 1 <-  2  <-  3      4  ->  5  ->  None
##            p      c      n 
## N <- 1 <-  2  <-  3  <-  4      5  ->  None
##                   p      c      n 
## N <- 1 <-  2  <-  3  <-  4  <-  5      None
##                          p      c      n 



def reverse(head):
    if head is None or head.next is None: 
        return head
    
    prev = None
    curr = head
    while curr is not None:
        next_node = curr.next
        curr.next = prev
        prev = curr
        curr = next_node
    return prev


     