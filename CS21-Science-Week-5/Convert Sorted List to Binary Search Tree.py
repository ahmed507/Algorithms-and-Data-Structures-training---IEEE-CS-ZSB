# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def sortedListToBST(self, head):
        if head is None:
            return None

        mid = self.get_mid(head)
        root = TreeNode(mid.val)
        if head == mid:
            return root
        root.left = self.sortedListToBST(head)
        root.right = self.sortedListToBST(mid.next)
        return root

    def get_mid(self, head):
        slow = head
        fast = head
        prev = head
        while fast is not None and fast.next is not None:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        if prev is not None:
            prev.next = None
        return slow
