vowels = ['a', 'o', 'y', 'e', 'u', 'i']
a = input()
for c in a:
    if c.lower() not in vowels:
        print('.{}'.format(c.lower()),end='')
