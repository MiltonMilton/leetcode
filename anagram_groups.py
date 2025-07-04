from typing import List


class Solution:

    def get_letters(self, s: str) -> dict:
        d_letter = {}
        for letter in s:
            if letter not in d_letter.keys():
                d_letter[letter] = 1
            else:
                d_letter[letter] += 1
        return d_letter

    def get_letters_key(self, d: dict) -> str:
        output = ""
        for k in sorted(d.keys()):
            output += f"{k}:{d[k]};"
        return output

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}
        for s in strs:
            s_letters = self.get_letters(s)
            s_letters_key = self.get_letters_key(s_letters)
            if s_letters_key in anagrams.keys():
                anagrams[s_letters_key] += [s]
            else:
                anagrams[s_letters_key] = [s]
        import json
        print( json.dumps(anagrams, indent=4) )
        return [anagrams_group for anagrams_group in anagrams.values()]

if __name__ == "__main__":
    s = Solution()
    strs = ["act","pots","tops","cat","stop","hat"]
    output = s.groupAnagrams(strs)
    print(output)