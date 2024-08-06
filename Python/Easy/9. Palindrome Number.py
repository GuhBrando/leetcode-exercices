class Solution:
    def isPalindrome(self, x: int) -> bool:
        y = str(x)[::-1]
        print(y)
        if str(x) == y:
            return True
        return False

print(Solution().isPalindrome(10))