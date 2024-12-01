class Solution:
    
    def lenoflongestsubstring(self,s:str)-> int:
        charset=set()
        l=0
        res=0
        for r in range(len(s)):
            while s[r] in charset:
                charset.remove(s[l])
                l+=1
            charset.add(s[r])
            res=max(res,r-l+1)
        return res

if __name__ == "__main__":
    s = "thisismyroom"
    p="thisismylab"
    s1 = Solution() 
    s2=Solution()
    result1 = s1.lenoflongestsubstring(s) 
    result2=s2.lenoflongestsubstring(p)
    print(result1,result2)