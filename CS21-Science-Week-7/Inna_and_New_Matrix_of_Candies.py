def max_moves(n):
    out = []
    for i in range(n):
        matrix = input()
        g = matrix.find('G')
        s = matrix.find('S')
        if g>s:
            return -1
        else:
            if s - g not in out:
                out.append(s - g)
    return len(out)
    
n,m = map(int,input().split())
print(max_moves(n))


