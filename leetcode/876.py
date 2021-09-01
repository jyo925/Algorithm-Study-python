# 러너 기법 사용 o(n), o(1)
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def middleNode(self, head: ListNode) -> ListNode:

        slow = head
        fast = head
        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next

        if fast.next:
            slow = slow.next
        return slow


# 리스트를 노드로 변경하는 작업
tmp = [1, 2, 3, 4, 5, 6]
node = ListNode(tmp[0])
crnt_node = node
for i in tmp[1:]:
    crnt_node.next = ListNode(i)
    crnt_node = crnt_node.next

print(Solution.middleNode('', node))