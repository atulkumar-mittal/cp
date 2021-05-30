def find_majority_element(a):
    res = 0
    count = 1
    i = 1
    while i < len(a):
        if a[res] == a[i]:
            count += 1
        else:
            count -= 1
        if count == 0:
            res = i
            count = 1
        i += 1
    print('maj element may be : index:{}, element:{}'.format(res,a[res]))
    count = 0
    i = 0
    while i < len(a):
        if a[i] == a[res]:
            count += 1
        i += 1
    if count <= int(len(a) / 2):
        print('not found')
    print('maj element is : {}'.format(a[res]))


find_majority_element([8, 1, 8, 1, 8, 1, 8])
