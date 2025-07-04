class Solution:
    def myAtoi(self, s: str) -> int:
        MAX = 2**31
        MIN = -2**31
        numbers = ["0","1","2","3","4","5","6","7","8","9"]
        # skip left white spaces
        s = s.lstrip()
        # check sign
        if s[0] == "-":
            s = s[1:]
            sign = -1
        elif s[0] == "+":
            s = s[1:]
            sign = 1
        elif s[0] in numbers:
            sign = 1
        else:
            return 0
        str_number = ""
        for char in s:
            if char in numbers:
                str_number += char
            else:
                break
        if not str_number:
            return 0
        number = sign * int(str_number)
        if number >= MAX:
            number =  MAX -1
        if number <= MIN:
            number = MIN
        return number

if __name__ == '__main__':
    s = Solution()
    print(s.myAtoi("42"))