class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        l={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        res=0
        for i in range(len(s)-1):
                    if(l[s[i]]<l[s[i+1]]):
                        res-=l[s[i]]
                    else:
                        res+=l[s[i]]
        return res+l[s[-1]]
