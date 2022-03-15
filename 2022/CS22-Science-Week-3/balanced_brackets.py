def isBalanced(s):
    brakets = {"{":"}",
               "(":")",
               "[":"]"}
    temp = []
    if len(s)%2!=0:
        return "NO"
    for i in range(len(s)):
        if s[i] == "{" or s[i] == "(" or s[i] == "[":
            temp.append(s[i])
        else:
            if len(temp) == 0 or brakets[temp[-1]] != s[i]:
                return "NO"
            temp.pop(-1)

    if len(temp)==0:
        return "YES"
    else:
        return "NO"

for i in range(int(input())):
    print(isBalanced(input()))