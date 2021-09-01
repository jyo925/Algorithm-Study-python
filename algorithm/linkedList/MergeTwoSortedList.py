# 두개의 정렬된 연결리스트를 병합하기
# o(m+n), o(1)
# 더미노드 사용

from typing import List


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def createList(in_list: List[int]) -> ListNode:
    if len(in_list) == 0:
        raise RuntimeError("in_list must have data")
    head_node = ListNode(in_list[0])
    last_node = head_node
    for idx in range(1, len(in_list)):
        node = ListNode(in_list[idx])
        last_node.next = node
        last_node = node
    return head_node


def printNodes(node: ListNode):
    crnt_node = node
    while crnt_node is not None:
        print(crnt_node.val, end=' ')
        crnt_node = crnt_node.next
    print()


class MergeTwoLists:
    def iterativeWay(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy_node = ListNode(0)
        crnt_node = dummy_node
        node1 = l1
        node2 = l2

        while node1 and node2:
            val1 = node1.val
            val2 = node2.val
            if val1 <= val2:
                crnt_node.next = node1
                node1 = node1.next
            else:
                crnt_node.next = node2
                node2 = node2.next
            crnt_node = crnt_node.next

        # 둘 중 한쪽만 남으면 남은 노드를 뒤에 연결
        if node1:
            crnt_node.next = node1
        else:
            crnt_node.next = node2

        return dummy_node.next

    # 재귀로도 구현 가능(참고)
    # 재귀는 공간복잡도  o(m+n)
    def recursiveWay(self, l1: ListNode, l2: ListNode) -> ListNode:
        # exit conditions
        if l1 is None:
            return l2
        elif l2 is None:
            return l1

        if l1.val <= l2.val:
            l1.next = self.recursiveWay(l1.next, l2)
            return l1
        else:
            l2.next = self.recursiveWay(l1, l2.next)
            return l2


if __name__ == "__main__":
    list1 = createList([1, 3, 5, 7])
    list2 = createList([1, 2, 3, 4])

    merger = MergeTwoLists()
    merged_head = merger.iterativeWay(list1, list2)
    printNodes(merged_head)
