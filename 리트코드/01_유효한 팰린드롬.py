import re
# s = "A man, a plan, a canal: Panama"
class Solution:
    def isPalindrome(self, s: str) -> bool:

        # 아래 세 줄만 제출
        s = s.lower()
        s = re.sub('[^a-z0-9]', '', s)
        return s == s[::-1]


# print(Solution.isPalindrome(0, s))