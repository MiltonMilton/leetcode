class Solution:
    def reverse(self, x: int) -> int:
        sign = 1 if x > 0 else -1
        str_number = str(abs(x))
        reversed_str_number = str_number[::-1]
        reversed_number = int(reversed_str_number)
        reversed_signed_number = sign * reversed_number
        return reversed_signed_number

if __name__ == "__main__":
    s = Solution()
    s.reverse(120)