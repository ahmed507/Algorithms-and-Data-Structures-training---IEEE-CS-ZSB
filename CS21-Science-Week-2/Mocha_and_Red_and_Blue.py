t = int(input())
for _ in range(t):
    n = int(input())
    s = list(input().strip())
    i = 0
    miss_n = s.count("?")
    while i + 1 != len(s):
        if s[i] == "R" and s[i + 1] == "?":
            s[i + 1] = "B"
        elif s[i] == "B" and s[i + 1] == "?":
            s[i + 1] = "R"
        i += 1
    if miss_n == len(s):
        s[0] = 'B'
        for k in range(len(s)):
            if k + 1 != len(s) and s[k] == 'B':
                s[k + 1] = 'R'
            elif k + 1 != len(s) and s[k] == 'R':
                s[k + 1] = 'B'
    else:
        while i != 0:
            if s[i] == "R" and s[i - 1] == "?":
                s[i - 1] = "B"
            elif s[i] == "B" and s[i - 1] == "?":
                s[i - 1] = "R"
            i -= 1

    print("".join(s))
