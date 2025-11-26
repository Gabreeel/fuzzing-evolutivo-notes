import random

def fuzzer(max_length: int = 100, char_start: int = 32, char_range: int = 32) -> str:
    """A string of up to `max_length` characters
       in the range [`char_start`, `char_start` + `char_range`)"""
    string_length = random.randrange(0, max_length + 1)
    out = ""
    for i in range(0, string_length):
        out += chr(random.randrange(char_start, char_start + char_range))
    return out

#print(fuzzer(100, 1, 100))
#print(fuzzer(100, 100, 0))
#print(fuzzer(100, 10, ord('0')))
print(fuzzer(100, ord('0'), 10))