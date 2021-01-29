'''
Reverse a singly linked list.

Example:

Input: 1->2->3->4->5->NULL
Output: 5->4->3->2->1->NULL
Follow up:

A linked list can be reversed either iteratively or recursively. Could you implement both?
'''
    
def reverseList(self, head):
    prev = None
    while head:
        curr = head
        head = head.next
        curr.next = prev
        prev = curr
    return prev

#Recursion

class Solution:
# @param {ListNode} head
# @return {ListNode}
def reverseList(self, head):
    return self._reverse(head)

def _reverse(self, node, prev=None):
    if not node:
        return prev
    n = node.next
    node.next = prev
    return self._reverse(n, node)

#my code
    def reverseList(self, head: ListNode) -> ListNode:
        return self._recursive(head, head.next)
    
     # could not understand where wrong..       
    def _recursive(self, curr, right):
        
        while right: #while is for iterative, here should use if
            
            right_new = right.next
            right.next = curr
            return self._recursive(right, right_new)
        return curr


        def reverseList(self, head: ListNode) -> ListNode:
        prev = None
        while head:
            new_head = head.next
            head.next = prev
            prev = head
            head = new_head
        return prev