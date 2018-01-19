class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __str__(self):
        temp = self
        s = []
        while temp:
            s.append(str(temp.val))
            temp = temp.next
        return ' -> '.join(s)

class LeetList:
    def __init__(self, l):
        dummy = ListNode(None)
        current = dummy
        for e in l:
            current.next = ListNode(e)
            current = current.next
        self.head = dummy.next


