def numDecodings(s):
    n = len(s)
    count = [0] * (n + 1)
    count[0] = 1
    count[1] = 0 if s[0] == "0" else 1
    for i in range(2, n + 1):
        count[i] = 0
        if (s[i - 1] > '0'):
            count[i] = count[i - 1]
        if (s[i - 2] == '1' or
           (s[i - 2] == '2' and
            s[i - 1] < '7') ):
            count[i] += count[i - 2]
 
    return count[n]


a = "11106"
print(numDecodings(a))
