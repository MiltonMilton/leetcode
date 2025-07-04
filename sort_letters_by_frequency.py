def sort_letters_by_frequency(s: str) -> str:
    letter_count = {}
    for letter in s:
        letter_count[letter] = letter_count.get(letter, 0) + 1
    letter_lists = [[] for _ in range(len(s))]
    for letter, count in letter_count.items():
        letter_lists[count - 1].append(letter)
    output = ''
    for letter_list in letter_lists[::-1]:
        if len(letter_list) > 1:
            letter_list.sort()
        output += ''.join(letter_list)
    return output

if __name__ == '__main__':
    print(sort_letters_by_frequency("aabbbcc"))
    print(sort_letters_by_frequency("abcdefgg"))
