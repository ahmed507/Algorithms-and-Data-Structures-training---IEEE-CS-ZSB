import collections
class Solution(object):
    def minWindow(self, s, t):
        if len(s) < len(t):
            return ""
        
        hashmap = collections.Counter(t)
        counter = len(t)
        min_window = ""
        start=0
        
        
        for end in range(len(s)):
            if hashmap[s[end]] > 0:
                counter -= 1
            hashmap[s[end]] -= 1
            
            while counter == 0:
                length = end - start + 1
                
                if not min_window or len(min_window) > length:
                    min_window = s[start:end+1]
                
                hashmap[s[start]] += 1

                if hashmap[s[start]] > 0:
                    counter += 1
                
                start += 1
        return min_window
