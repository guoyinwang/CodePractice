class Solution(object):
    def isPalindrome(self, x):
        """
            :type x: int
            :rtype: bool
            """
        y =0
        if (x<0):
            return False
        x1=x
        while(x/10 != 0):
            y = y*10 + x%10
            x=x/10;
        y = y*10+x%10
        if (x1==y):
            return True
        else:
            return False
if __name__ =='__main__':
    x = -23
    a = Solution()
    result =  a.isPalindrome(x)
    print result