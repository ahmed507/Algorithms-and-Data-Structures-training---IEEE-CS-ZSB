def isValid(s):
    open = ["(","{","["]
    close = [")","}","]"]
    temp = []
    for i in range(len(s)):
        if s[i] in open:
            temp.append(s[i])
        elif s[i] in close:
            if len(temp) == 0:
                return False
            for j in range(len(temp)-1,-1,-1):
                if close[open.index(temp[j])]==s[i]:
                    temp.pop()
                    break
                else:
                    return False
        else:
            return False
    if len(temp) == 0:
        return True
    else:
        return False


s = input()
if isValid(s):
    print("Yes")
else:
    print("No")
                
                