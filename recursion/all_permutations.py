def remove_char_at(st, i):
    if i > len(st) or i < 0:
        return st
    return st[: i] + st[min(i + 1, len(st)):]


def all_permutation(st, bag):
    if len(st) == 1:
        bag.append(st)
        return
    i = 0
    while i < len(st):
        cb = []
        all_permutation(remove_char_at(st, i), cb)
        bag.extend([st[i] + s for s in cb])  # add current character to all child permutations
        print(bag)
        i += 1


# print(remove_char_at('abc', 0))
# print(remove_char_at('abc', 1))
# print(remove_char_at('abc', 2))
# print(remove_char_at('abc', 3))
# print(remove_char_at('abc', -1))

b = []
all_permutation('abc', b)
print(b)
