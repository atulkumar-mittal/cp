def find_max_sum_subarray(a):
    print('Input array: {}'.format(a))
    max_so_far = -29383474746593756338
    curr_sum = 0
    i = 0
    while i < len(a):
        curr_sum = max(curr_sum + a[i], a[i])
        max_so_far = max(max_so_far, curr_sum)
        i += 1
    print(max_so_far)

#https://www.youtube.com/watch?v=II6ziNnub1Q&list=PLgUwDviBIf0pmWCl2nepwGDO05a0-7EfJ
#https://www.youtube.com/watch?v=63fPPOdIr2c&t=889s

find_max_sum_subarray([-1, -2, 0, 1, -8, -6])
find_max_sum_subarray([1, 2, 3, -293, 2, 4, 44])
find_max_sum_subarray([0, 0, 0, 0])
find_max_sum_subarray([-1, -2, -3, -4])
find_max_sum_subarray([1,2,3])
find_max_sum_subarray([-1])
