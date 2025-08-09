class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        gcd = str1 if len(str1)<len(str2) else str2
        def isDivisible(word,div):
            l,L = len(div),len(word)
            if L%l != 0:
                return False
            i,j = 0,0
            for i in range(L):
                if word[i]!=div[j]:
                    return False
                j = (j+1)%l
            return True
        while len(gcd)>0:
            if isDivisible(str1,gcd) and isDivisible(str2,gcd):
                return gcd
            gcd  = gcd[:-1]
        return ''
        
