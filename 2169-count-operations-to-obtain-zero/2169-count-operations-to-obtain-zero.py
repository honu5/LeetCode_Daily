class Solution(object):
    def countOperations(self, num1, num2):
        """
        :type num1: int
        :type num2: int
        :rtype: int
        """
        count=0
        while True:
            if num1==0 or num2==0:
                return count
            if num1>num2:
                num1-=num2
                count+=1
            elif num2>num1:
                num2-=num1
                count+=1
            else:
                count+=1
                return count
        