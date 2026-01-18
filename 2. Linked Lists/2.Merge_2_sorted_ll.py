from common import *

def merge_two_sorted_ll(head1, head2):
    if head1 is None:
        return head2
    if head2 is None:
        return head1
    
    final_head=None
    final_tail=None
    
    while head1 is not None and head2 is not None:
        if head1.data<head2.data:
            if final_head==None:
                final_head=head1
                final_tail=head1
            else:
                final_tail.next=head1
                final_tail=head1
            head1=head1.next
        else:
            if final_head==None:
                final_head=head2
                final_tail=head2
            else:
                final_tail.next=head2
                final_tail=head2
            head2=head2.next
    
    if head1 is not None:
        final_tail.next=head1
    if head2 is not None:
        final_tail.next=head2
        
    return final_head