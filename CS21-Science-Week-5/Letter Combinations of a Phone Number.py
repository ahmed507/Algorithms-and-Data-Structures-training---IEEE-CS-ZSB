def letterCombinations(digits):
    numbers = {
        "2": ["a", "b", "c"],
        "3": ["d", "e", "f"],
        "4": ["g", "h", "i"],
        "5": ["j", "k", "l"],
        "6": ["m", "n", "o"],
        "7": ["p", "q", "r", "s"],
        "8": ["t", "u", "v"],
        "9": ["w", "x", "y", "z"]
    }
    out = []
    temp = [""]
    while len(temp) !=0:
        t = temp.pop()
        if len(t) == len(digits):
            out.append(t)
        else:
            for i in numbers[digits[len(t)]]:
                temp.append(t+i)
    if out[0] =="":
        out.pop()
    return out
