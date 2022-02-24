def check_r(r):
    r = int(r)
    if r >= 256:
        r %= r
        return r
    while r < 0:
        r += 256
    return r


def FHBZMIPS(operations):
    r = 0
    x = 0
    i = 0
    counter = 0
    while i != len(operations):
        x = operations[i][0]
        if x == 'add':
            r += int(operations[i][1])
            r = check_r(r)
        elif x == 'sub':
            r -= int(operations[i][1])
            r = check_r(r)
        elif x == 'mul':
            r *= int(operations[i][1])
            r = check_r(r)
        elif x == 'div':
            r /= int(operations[i][1])
            r = check_r(r)
        elif x == 'and':
            r = int(operations[i][1]) & r
            r = check_r(r)
        elif x == 'or':
            r = int(operations[i][1]) | r
            r = check_r(r)
        elif x == 'xor':
            r = int(operations[i][1]) ^ r
            r = check_r(r)
        elif x == 'gotoif':
            if int(operations[i][1]) <= r:
                i = int(operations[i][2]) - 1
                if counter == 10000:
                    return "execucao infinita"
                counter += 1
                continue
            else:
                continue
        else:
            return r
        i += 1


for _t in range(int(input())):
    n = int(input())
    operations = []
    r = 0
    for _ in range(n):
        op = list(input().split())
        operations.append(op[1:])
    print(FHBZMIPS(operations))