class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        frequency = 0
        char = chars[0]
        pointer = 0
        for i in chars:
            if i == char:
                frequency += 1
            else:
                if frequency == 1:
                    chars[pointer] = char
                    char = i
                    frequency = 1
                    pointer += 1
                else:
                    chars[pointer] = char
                    char = i
                    chars[pointer + 1:pointer + 1 + len(str(frequency))] = list(str(frequency))
                    pointer += len(str(frequency)) + 1
                    frequency = 1
        if frequency == 1:
            chars[pointer] = char
            pointer += 1
        else:
            chars[pointer] = char
            char
            chars[pointer + 1:pointer + 1 + len(str(frequency))] = list(str(frequency))
            pointer += len(str(frequency)) + 1
        return pointer
              
                