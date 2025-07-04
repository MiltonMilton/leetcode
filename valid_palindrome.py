import string


class Solution:
    def isPalindrome(self, s: str) -> bool:
        #only azAZ09
        clean_s  = [c.lower() for c in s if c in string.ascii_letters + string.digits ]
        return clean_s == list(reversed(clean_s))

if __name__ == '__main__':
    solution = Solution()
    s = "Was it a car or a cat I saw?"
    print(solution.isPalindrome(s))