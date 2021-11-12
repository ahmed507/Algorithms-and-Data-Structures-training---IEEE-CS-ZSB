'''
def bt(board,word,i,j,k,counter):
    # print(i,j,k,counter)
    if counter == len(word):
        return counter
    if i<len(board)-1:
        if board[i+1][j]==word[k]:
            # print(1)
            return bt(board,word,i+1,j,k+1,counter+1)
    if i>0:
        if board[i-1][j]==word[k]:
            # print(2)
            return bt(board,word,i-1,j,k+1,counter+1)
    if j<len(board[0])-1:
        if board[i][j+1]==word[k]:
            # print(3)
            return bt(board,word,i,j+1,k+1,counter+1)
    if j>0:
        if board[i][j-1]==word[k]:
            # print(4)
            return bt(board,word,i,j-1,k+1,counter+1)
    else:
        # print(5)
        # print("counter",counter)
        return counter
'''
def dfs(board, i, j, word):
    if len(word) == 0: # all the characters are checked
        return True
    if i<0 or i>=len(board) or j<0 or j>=len(board[0]) or word[0]!=board[i][j]:
        return False
    tmp = board[i][j]  # first character is found, check the remaining part
    board[i][j] = "#"  # avoid visit agian 
    # check whether can find "word" along one direction
    res = dfs(board, i+1, j, word[1:]) or dfs(board, i-1, j, word[1:]) \
    or dfs(board, i, j+1, word[1:]) or dfs(board, i, j-1, word[1:])
    board[i][j] = tmp
    return res
def exist(board,word):
    for i in range(len(board)):
        for j in range(len(board[i])):
            if dfs(board, i, j, word):
                return True

board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
word = "SEE"
if exist(board,word):
    print("yes")
else:
    print("No")