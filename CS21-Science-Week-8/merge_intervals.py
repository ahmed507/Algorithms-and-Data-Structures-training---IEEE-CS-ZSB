def merge(intervals):
    intervals = sorted(intervals,key=lambda l:l[0])
    out = [intervals[0]]
    intervals.remove(intervals[0])
    i = 0
    while len(intervals)!=0:
        if intervals[0][0] in range(out[i][0],out[i][1]+1):
            old = out[-1]
            out.pop()
            out.append([min(old[0],intervals[0][0]),max(old[1],intervals[0][1])])
            intervals.remove(intervals[0])
        else:
            out.append(intervals[0])
            intervals.remove(intervals[0])
            i +=1
    return out

intervals = [[1,3],[2,6],[8,10],[15,18]]
print(merge(intervals))