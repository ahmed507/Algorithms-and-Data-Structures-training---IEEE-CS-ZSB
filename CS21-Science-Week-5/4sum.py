def fourSum(nums, target):
    nums.sort()
    out = []
    for i in range(len(nums)-3):
        for j in range(i+1,len(nums)-2):
            l = j+1
            r = len(nums)-1
            while l<r:
                sum = nums[i]+nums[j]+nums[l]+nums[r]
                if sum == target:
                    out.append([nums[i],nums[j],nums[l],nums[r]])
                    l +=1
                    r-=1
                elif sum <target:
                    l+=1
                else:
                    r-=1
    result = []
    for k in out:
        if k not in result:
            result.append(k)

    return result

print(fourSum([2,2,2,2,2],8))