class Node:

    data = None
    next = None

    def __init__(self, data):
        self.data = data


def create_list(data):
    if data:
        head = None
        prev = head
        for x in data:
            node = Node(x)
            if head is None:
                head = node
                prev = head
            prev.next = node
            prev = node
        return head


def iterate_list(head):
    while head is not None:
        print(head.data)
        head = head.next


def merge_lists(l1, l2, a, b):
    before_a = None
    after_b = None
    l2_tail = get_last_node(l2)
    prev = None
    curr = l1
    for i in range(1, b+1):
        if i == a:
            before_a = prev
        if i == b:
            after_b = curr.next
            break
        prev = curr
        curr = curr.next

    if before_a is None:
        l2_tail.next = after_b
        return l2
    else:
        before_a.next = l2
        l2_tail.next = after_b
        return l1


def get_last_node(lst):
    while lst.next is not None:
        lst = lst.next
    return lst


if __name__ == '__main__':
    list1 = create_list([1, 2, 3, 4, 5, 12, 12, 14, 18])
    list2 = create_list([6, 7])

    new_l = merge_lists(list1, list2, 2, 3)
    iterate_list(new_l)
