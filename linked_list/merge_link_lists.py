'''
Give two linked list, merge the second list inside first list at given position.
The second list can be added at the start, mid or end of first list
if pos = 0, then l2->l1
if pos = len(l1) then l1>l2
if pos = somewhere_mid(l1) then l1--mid-l2--mid+1--l1END
'''


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


def get_last_node(lst):
    while lst.next is not None:
        lst = lst.next
    return lst


def find_len(l):
    i = 1
    while l.next is not None:
        l = l.next
        i += 1
    return i


def merge_lists_new(l1, l2, p):
    if p == 0:
        print('before l1')
        l2_tail = get_last_node(l2)
        l2_tail.next = l1
        return l2
    if p >= find_len(l1):
        print('after l1')
        l1_tail = get_last_node(l1)
        l1_tail.next = l2
        return l1
    print('between')
    before_l2 = l1
    after_l2 = l1.next
    for i in range(1, p):
        if i == p:
            break
        before_l2 = after_l2
        after_l2 = after_l2.next
    before_l2.next = l2
    l2_tail = get_last_node(l2)
    l2_tail.next = after_l2
    return l1


if __name__ == '__main__':
    list1 = create_list([1, 2, 3, 4, 5, 12, 12, 14, 18])
    list2 = create_list([6, 7])
    pos = 8
    new_l = merge_lists_new(list1, list2, pos)
    iterate_list(new_l)
