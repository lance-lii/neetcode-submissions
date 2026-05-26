class Solution(object):
    def isPalindrome(self, x):
        s = str(x)
        cleaned = [c.lower() for c in s if c.isalnum()]
        return cleaned == cleaned[::-1]