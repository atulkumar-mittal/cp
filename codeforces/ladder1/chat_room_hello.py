# s1 = input()
# s2 = 'helpo'
# i = 0
# j = 0
# while i < len(s1) and j < 5:
#     if s1[i] == s2[j]:
#         while s1[i+1] == s2[j]:
#             i += 1
#         j += 1
#     else:
#         j = 0
#     i += 1
# if j == 5:
#     print('YES')
# else:
#     print('NO')
#

def freq_method(s1):
    s2 = 'hello'
    s1_char = []
    s1_freq = []
    s2_char = []
    s2_freq = []
    s1_char.append(s1[0])
    s1_freq.append(1)
    s2_char.append(s2[0])
    s2_freq.append(1)

    i = 1
    while i < len(s1):
        if s1_char[-1] == s1[i]:
            s1_freq[-1] += 1
        else:
            s1_char.append(s1[i])
            s1_freq.append(1)
        i += 1

    i = 1
    while i < len(s2):
        if s2_char[-1] == s2[i]:
            s2_freq[- 1] += 1
        else:
            s2_char.append(s2[i])
            s2_freq.append(1)
        i += 1

    i = 0
    j = 0
    while i < len(s1_char) and j < 4:
        if s1_char[i] == s2_char[j] and s1_freq[i] >= s2_freq[j]:
            j += 1
        else:
            j = 0
        i += 1
    if j == 4:
        print('YES')
    else:
        print('NO')


freq_method('ahhelllllooop')
