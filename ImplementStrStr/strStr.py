class Solution(object):
    def strStr(self, haystack, needle):
        """
            :type haystack: str
            :type needle: str
            :rtype: int
            """
        n = len(haystack)
        m = len(needle)
        compare = 0
        for i in range(0,n-m+1):
            compare =1
            for j in range(0,m):
                if not (needle[j]==haystack[i+j]):
                    compare =0
            if compare ==1:
                return i
        return -1
if __name__ == '__main__':
    haystack = "a"
    needle = "a"
    a = Solution()
    result = a.strStr(haystack,needle)
    print result