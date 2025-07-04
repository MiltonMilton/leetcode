class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        substrings = []
        current_substring = ''
        for _c in s:
            if _c not in current_substring:
                current_substring += _c
            if current_substring in substrings:
                current_substring = ''
            else:
                substrings.append(current_substring)
        return max([len(substring) for substring in substrings])


