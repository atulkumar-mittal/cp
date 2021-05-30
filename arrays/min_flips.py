'''
    There is an array of 1s and 0s. The 1s represent land and 0 represents water.
    We have to find out number of lands and numbers of waters and minimum of it would be the required flips
'''


def min_flips_to_make_same(a):
    waters = 0
    lands = 0
    i = 1
    count = 0
    while i < len(a):
        if a[i] == a[i - 1]:
            i += 1
            count += 1
            continue
        if a[i] == 1:
            waters += 1
            count = 1
        else:
            lands += 1
            count = 1
        i += 1
    if count > 0:
        if a[i-1] == 1:
            lands += 1
        else:
            waters += 1
    print('lands: {} and waters: {}'.format(lands, waters))


min_flips_to_make_same([1, 0, 0, 0, 1, 1])
min_flips_to_make_same([1, 1, 1])
min_flips_to_make_same([0, 0, 0,1])
min_flips_to_make_same([1,0,1,0,0,1])
min_flips_to_make_same([0,0,0,0])
