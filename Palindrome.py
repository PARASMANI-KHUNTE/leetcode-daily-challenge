class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """

        s = []
        r = []
        q = str(x)
        for j in range(len(q)):
            s.append(q[j])

        for i in range(len(q)-1,-1,-1):
            r.append(q[i])
        

        if s == r:
            return True
        else:
            return False
            
            











a = Solution()
anum = 121

print(a.isPalindrome(anum))
        