np = input().split(' ')
n = int(np[0])
p = int(np[1])


def return_max_lights(n, p):
    scanline = [0] * (p + 1)
    lights = n
    while lights > 0:
        xiri = input().split(' ')
        if len(xiri) > 2:
            return n
        xi = int(xiri[0])
        ri = int(xiri[1])

        scanline[max(0, xi - ri)] += 1
        scanline[min(p, xi + ri + 1)] -= 1
        lights -= 1

    current_dark = 1 if scanline[0] != 1 else 0
    maxdark = 0
    for i in range(1, len(scanline)):
        scanline[i] += scanline[i - 1]
        if scanline[i] != 1:
            current_dark += 1
        else:
            maxdark = max(maxdark, current_dark)
            current_dark = 0
    return max(maxdark, current_dark)


res = return_max_lights(n, p)
print(res)
