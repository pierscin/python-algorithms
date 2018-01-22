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

    def __eq__(self, other):
        if type(self) != type(other): return False

        temp = self
        other_temp = other

        while temp and other_temp and temp.val == other_temp.val:
            temp, other_temp = temp.next, other_temp.next

        return temp is None and other_temp is None

    # TODO: typing
    @staticmethod
    def from_list(l):
        dummy = node = ListNode(None)

        for e in l:
            node.next = ListNode(e)
            node = node.next
        return dummy.next

    def to_list(self):
        values = []

        node = self
        while node:
            values.append(node.val)
            node = node.next

        return values
