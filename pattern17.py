class Solution:
    def pattern17(self, n):
        for i in range(n):

            for j in range(n-i-1):
                print(" ", end=" ")

            ch = 65
            for j in range(2*i + 1):
                print(chr(ch), end=" ")

                if j < i: # j < (2*i + 1) // 2
                    ch += 1 
                else:                    
                    ch -= 1

            print()
obj=Solution()
n=int(input())            
obj.pattern17(n)