from commonLL import *

def Merger2sortedll(head1,head2):
    
    if head1 is None:
        return head2
    if head2 is None:
        return head1
    
    finalhead=None
    finaltail=None
    
    while head1 is not None and head2 is not None:
        if(head1.data<head2.data):
            if(finalhead==None):
                finalhead=head1
                finaltail=head1
            else:
                finaltail.next=head1
                finaltail=head1
        else:
            if (finalhead==None):
                finalhead=head2
                finaltail=head2
            else:
                finaltail.next = head2
                finalhead=head2
            head2=head2.next

	if head1 is not None:
            finaltail.next=head1

	if head2 is not None:
            finaltail.next=head2

		return finalhead
        
            
            