
# Definition for singly-linked list.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        def reverse(node: ListNode, prev: ListNode = None):
            if not node:
                return prev
            n, node.next = node.next, prev
            return reverse(n, node)

        return reverse(head)


a = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, None)))))

print(Solution.reverseList("", a).val)


