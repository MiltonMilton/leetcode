import sys

def greatest_palindrome(n:str) -> int:
    counter = {}
    for digit in str(n):
        counter[digit] = counter.get(digit, 0) + 1
    ordered_counter = sorted(counter.items(), key=lambda x: x[0], reverse=True)
    side_digits = []
    center_digits = []
    for digit, count in ordered_counter:
        if count > 1:
            if count % 2 == 0:
                side_digits.append((digit, count))
            else:
                side_digits.append((digit, count - 1))
                center_digits.append(digit)
        else:
            center_digits.append(digit)
    side = ''
    for digit, count in side_digits:
        side += digit * int(count / 2)
    center = max(center_digits) if center_digits else ''
    if int(side) > 0:
        return int(side + center + side[::-1])
    else:
        return int(center) if center else None

if __name__ == "__main__":
    # how to test? run on the current directory: "python3 greatest_palindrome.py < greatest_palindrome_input.txt"
    lines = sys.stdin.read().splitlines()
    t = int(lines[0])
    for i in range(1, t + 1):
        n = lines[i]
        print(greatest_palindrome(n))
