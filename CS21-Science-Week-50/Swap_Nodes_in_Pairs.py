# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        listnode = ListNode(0)
        listnode.next = head
        current = listnode
        while current.next is not None and current.next.next is not None:
            temp1 = current.next
            temp2 = current.next.next
            temp3 = current.next.next.next
            current.next = temp2
            temp2.next = temp1
            temp1.next = temp3
            current = temp1
        return listnode.next
