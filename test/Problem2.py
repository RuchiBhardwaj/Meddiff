class Solution:
    def isPalindrome(self, string: str) -> bool:
        s = string.lower()
        s = [char for char in s if char.isalnum()]
        return s == s[::-1]

s = "cbabc"
So = Solution()
print(So.isPalindrome(s))