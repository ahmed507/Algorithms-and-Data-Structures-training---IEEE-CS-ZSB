def maximal_sections(i,n,heights):
    counter = 1
    j = i
    while j > 0 and heights[j - 1] <= heights[j]:
        j -= 1
        counter += 1
    j = i
    while j < n - 1 and heights[j] >= heights[j + 1]:
        j += 1
        counter += 1
    return counter


n = int(input())
heights = list(map(int,input().split()))

max_section = 0
for i in range(n):
    max_section = max(max_section, maximal_sections(i,n,heights))
print(max_section)