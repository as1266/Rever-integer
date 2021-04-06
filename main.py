class Solution:
    def reverse(self, x: int) -> int:
        if (x == 0) or (x < 10) and (x > 0):
            answer = x
            return answer
        else:
            newN = str(x)
            newNumb= list(newN)
            answer = []

            for i in range(1,len(newNumb)):
                answer.append(newNumb[len(newNumb)-i])

            if newNumb[0] == '-':
                answer.insert(0,'-')
            else:
                answer.append(newNumb[0])
            
            answer = "".join(answer)
            answer= int(answer)
            
            if -2**31 <= answer <= (2**31)-1:
                return answer
            else:
                return 0
        

number= 1234
Mysolution = Solution()
Mysolution.reverse(number)
