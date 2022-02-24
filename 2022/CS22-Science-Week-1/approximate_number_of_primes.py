from math import log, e


def ln(x):
    return log(x, e)


n = int(input())
P = n / ln(n)
M = P * 1.25506
print("{:.1f}".format(P), "{:.1f}".format(M))
