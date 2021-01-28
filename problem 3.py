class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        import numpy as np
        if len(s)==0:
            d_max = 0
            return d_max
        templist = [s[0]]
        d_max = 1
        d_temp = 0
        for j in range(1,len(s)):
            if not s[j] in templist:
                templist.append(s[j])
                d_temp = len(templist)
            else:
                callist = np.array(templist)
                k = np.where(callist==s[j])[0][0]
                templist = templist[k+1:]
                templist.append(s[j])
                d_temp = len(templist)
            if d_temp > d_max:
                d_max = d_temp
        return d_max