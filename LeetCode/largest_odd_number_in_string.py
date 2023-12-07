# https://leetcode.com/problems/largest-odd-number-in-string/submissions/?envType=daily-question&envId=2023-12-07
class Solution:
    def largestOddNumber(self, num: str) -> str:
      i = len(num) - 1
      while i != -1:
        if int(num[i]) % 2 == 1:
            # Number is odd
            return num[0:i+1]
        i -= 1
      return ""