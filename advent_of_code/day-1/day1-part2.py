import re
text = open("test.txt", "r")
calibration_data = text.readlines()

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


def find_all_numbers_with_positions(s, number_words):
    result = {}

    for word, num in number_words.items():
        for match in re.finditer(word, s):
            result.setdefault(match.group(), []).append(match.start())

    for match in re.finditer(r"\d", s):
        result.setdefault(match.group(), []).append(match.start())

    for key in result:
        if len(result[key]) == 1:
            result[key] = result[key][0]

    return result


list_of_numbers = []
for line in calibration_data:
    line = line.replace("\n", "")

    num_dict = find_all_numbers_with_positions(line, number_words_to_digits)

    converted_dict = {}
    for key, value in num_dict.items():
        num_key = number_words_to_digits.get(key, key)

        if not isinstance(value, list):
            value = [value]

        converted_dict[num_key] = value

    min_index_num = str(min(converted_dict, key=lambda k: min(converted_dict[k])))
    max_index_num = str(max(converted_dict, key=lambda k: max(converted_dict[k])))

    list_of_numbers.append(int(f"{min_index_num}{max_index_num}"))


print(f"Solution Part 2: {sum(list_of_numbers)}")