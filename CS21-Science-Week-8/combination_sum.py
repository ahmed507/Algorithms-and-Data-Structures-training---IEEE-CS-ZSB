def dfs(target,nums,j,ans,path):
    if target<0:
        return
    if target==0:
        ans.append(path)
        return
    for i in range(j,len(nums)):
        dfs(target-nums[i],nums,i,ans,path+[nums[i]])


def combinationSum(candidates, target):
    ans = []
    path = []
    candidates.sort()
    dfs(target,candidates, 0, ans, path)
    return ans

print(combinationSum([2,3,5],8))
