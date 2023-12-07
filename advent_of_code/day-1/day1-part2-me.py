import re
testfile = open("test.txt",'r')

tests = testfile.readlines()

number_words_to_digits = {
    "zero": 0,
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
    "ten": 10,
    "eleven": 11,
    "twelve": 12,
    "thirteen": 13,
    "fourteen": 14,
    "fifteen": 15,
    "sixteen": 16,
    "seventeen": 17,
    "eighteen": 18,
    "nineteen": 19,
    "twenty": 20,
}


def find_all_numbers(case,number_words):

    result = {}

    for word,num in number_words.items():

        for match in re.finditer(word,case):
            result.setdefault(match.group(),[]).append(match.start())
    
    for match in re.finditer(r"\d", s):
        result.setdefault(match.group(), []).append(match.start())

    for key in result:
        if len(result[key]) == 1:
            result[key] = result[key][0]

    return result