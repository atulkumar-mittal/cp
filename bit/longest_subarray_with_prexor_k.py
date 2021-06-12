'''
Given an array of integers, find out the longest subarray for which xor of numbers is equal to K
arr = [2,5,6,1,0,3,5,6] K = 4 then possible options = [6,1,0,3] and [5,6,1,0,3,5]
output = 6 (len of largest)

The problem needs some thinking around xor properties
n ^ 0 = n
n ^ n = 0
a1^a2^a3 ^ an = K => a2^a3 ^ an ^K = a1
so that means if all prexors of a1,a2,a3,a4 are known to us and we find out a1^a2^a3^a4^K = a1^a2 then
a3^a4^K = 0
a3^a4 = K
'''


def find_largest_with_prexor_k(arr, k):
    prexor = 0
    hashing = {}
    maxlen = 0
    for i in range(len(arr)):
        prexor = prexor ^ arr[i]
        if prexor ^ k in hashing:
            maxlen = max(maxlen, i - hashing.get(prexor ^ k))
        if hashing.get(prexor) is None:
            hashing[prexor] = i
        print(
            'index: {}, prexor:{}, prexor^K : {}, maxlen:{}, hasing:{}'.format(i, prexor, prexor ^ k, maxlen, hashing))
    return maxlen


find_largest_with_prexor_k([2, 5, 6, 1, 0, 3, 5, 6], 4)
