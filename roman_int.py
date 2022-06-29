class Solution:
    def romanToInt(self, s: str) -> int:
        roman = {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        val=0
        s=s.upper()
        for i in range(len(s)): #XXV
            if i+1 < len(s) and roman[s[i]] < roman[s[i+1]]:
                val-=roman[s[i]]
                print(val)
            else:
                val+=roman[s[i]]
                print(val)
        return val
tan = Solution()
s = input(print("Enter the Roamn number to convert to Intiger:"))
run = tan.romanToInt(s)
print(run)
