class Solution:
    def longestPalindrome(self, s: str) -> str:
        s_len = len(s)
        palindrome_substrings = []
        for i in range(s_len):
            for j in range(i + 1, s_len):
                if s[i:j] == s[i:j][::-1]:
                    palindrome_substrings.append(s[i:j])
        max_length = max([len(p) for p in palindrome_substrings])
        return [
            p for p in palindrome_substrings if len(p) is max_length
        ][0] if palindrome_substrings else None