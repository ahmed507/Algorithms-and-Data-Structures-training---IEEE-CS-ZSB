import sys

def minimumMoves(grid, startX, startY, goalX, goalY):
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    n = len(grid)
    m = len(grid[0])
    queue = []
    visit = [ [sys.maxsize]*n for i in range(m)]
    queue.append([startX, startY, 0, -1])
    visit[startX][startY] = 0
    while queue:
        x, y, cost, d = queue[0]
        queue.pop(0)
        for z in range(4):
            i = x + dx[z]
            j = y + dy[z]
            if 0 <= i < n and 0 <= j < m and grid[i][j] == '.':
                if visit[i][j] > cost:
                    queue.append((i, j, cost + (d != z), z))
                    visit[i][j] = cost + (d != z)

    return visit[goalX][goalY]

grid = ['.X.','.X.', '...']
startX = 0
startY = 0
goalX = 0
goalY = 2
print(minimumMoves(grid,startX,startY,goalX,goalY))