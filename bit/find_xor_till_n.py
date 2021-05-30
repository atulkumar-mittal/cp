'''
Given a number n find the xor from 1 -> N
so if N = 5 -- the brute approach is given below
res = 0
for(i=1; i<=N; i++){
    res = res ^ i;
}
return res;
Find efficient approach
'''

# Solution

'''
so if we write xor of numbers from 1 to 10, we can see a pattern
'''
xor = 0
for i in range(1, 11):
    xor = (xor ^ i)
    print('Xor till {} is : {}'.format(i, xor))

'''
pattern is if n%4 ==0 or 1 or 2 or 3 you get a predictable xor
Complexity O(1)
'''


def find_xor_till_n(n):
    if n % 4 == 0:
        return n
    if n % 4 == 1:
        return 1
    if n % 4 == 2:
        return n + 1
    return 0


n = 7
xor = find_xor_till_n(n)
print('xor till {} is {}'.format(n, xor))
