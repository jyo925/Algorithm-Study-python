class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


head_node = ListNode(1)
head_node.next = ListNode(2)
head_node.next.next = ListNode(3)
head_node.next.next.next = ListNode(4)


# 반복문 출력
def printNodes(node: ListNode):
    crnt_node = node
    while crnt_node is not None:
        print(crnt_node.val, end=' ')
        crnt_node = crnt_node.next

    print()


# printNodes(head_node)
# print()


# 재귀 출력
def printNodeRecur(node: ListNode):
    print(node.val, end=' ')
    if node.next is not None:
        printNodeRecur(node.next)


# printNodeRecur(head_node)

# 단순 연결리스트 생성
class SLinkedList:
    def __init__(self):
        self.head = None

    # 맨 앞에 추가 o(1)
    def addAtHead(self, val):
        node = ListNode(val)
        node.next = self.head
        self.head = node

    # 맨 끝에 추가 o(n)
    def addBack(self, val):
        node = ListNode(val)
        crnt_node = self.head

        if crnt_node is None:
            self.addAtHead(val)
            return

        while crnt_node.next:
            crnt_node = crnt_node.next

        crnt_node.next = node

    # 특정 노드 탐색 o(n)
    def findNode(self, val):
        crnt_node = self.head
        while crnt_node.next:
            if crnt_node.val == val:
                return crnt_node
            crnt_node = crnt_node.next
        raise RuntimeError('Node not found')

    # 중간에 추가 o(1)
    # node = node1 의미
    # 1node -> new_node -> node2
    def addAfter(self, node, val):
        new_node = ListNode(val)
        new_node.next = node.next
        node.next = new_node

    # 특정 노드를 삭제하려면 특정 노드의 이전 노드를 알아야 하는데 복잡함
    # 여기서는 입력받은 노드의 다음 노드를 삭제 o(1)
    def deleteAfter(self, prev_node):
        if prev_node is not None:
            prev_node.next = prev_node.next.next

    # prev_node를 사용하여 연결리스트 내 특정 요소를 삭제하기

    def iterative(self, node: ListNode) -> ListNode:
        dummy_node = ListNode(0)
        dummy_node.next = slist.head

        crnt_node = slist.head
        prev_node = dummy_node

        while crnt_node:
            if crnt_node.val == 3:
                prev_node.next = crnt_node.next
                crnt_node = crnt_node.next
            else:
                crnt_node = crnt_node.next
                prev_node = prev_node.next
        return dummy_node.next

    # prev_node를 사용하지 않고 재귀를 사용하여 삭제하기
    def recursive(self, node: ListNode) -> ListNode:
        if not node:
            return None
        next_node = self.recursive(node.next)
        if node.val == 3:
            return next_node
        else:
            node.next = next_node
            return node


slist = SLinkedList()
# slist.addAtHead(1)
# slist.addAtHead(2)
# slist.addBack(3)
# printNodes(slist.head)
# node1 = slist.findNode(1)
# slist.addAfter(node1, 4)
# printNodes(slist.head)

# slist.addBack(4)
# printNodes(slist.head)

slist.addBack(3)
slist.addBack(3)
slist.addBack(5)
slist.addBack(7)
slist.addBack(3)
slist.addBack(1)
printNodes(slist.head)
printNodes(slist.iterative(slist.head))
