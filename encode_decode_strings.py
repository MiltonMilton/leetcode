from typing import List


class Solution:

    separator = "%%%%"
    empty_string = ""
    empty_string_code = "{{s}}"

    def encode_string(self, s: str) -> str:
        return self.empty_string_code if s == self.empty_string else s

    def decode_string(self, s: str) -> str:
        return self.empty_string if s == self.empty_string_code else s

    def encode(self, strs: List[str]) -> str:
        return self.separator.join([self.encode_string(s) for s in strs])

    def decode(self, s: str) -> List[str]:
        if s == "":
            return []
        return [self.decode_string(s) for s in s.split(self.separator)]


if __name__ == "__main__":
    s = Solution()
    encoded = s.encode([""])
    print(encoded)
    decoded = s.decode(encoded)
    print(decoded)