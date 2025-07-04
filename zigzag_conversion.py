class Solution:
    def convert(self, s: str, numRows: int) -> str:
        index = 1
        rows = {}
        direction = 1
        for character in s:
            if index in rows.keys():
               rows[index].append(character)
            else:
               rows[index] = [character]
            if index == numRows:
                direction = -1
            elif index == 1:
                direction = 1
            index += direction
        output = ""
        for i in range(numRows):
            output += "".join(rows[i+1])
        return output
