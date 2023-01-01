import textwrap

def wrap(string, max_width):
    breaked_word = []
    pointer = 0
    while pointer+max_width <len(string):
        breaked_word.append(string[pointer:pointer+max_width]+"\n")
        pointer+=max_width
    breaked_word.append(string[pointer:])
    return "".join(breaked_word)
        



if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
