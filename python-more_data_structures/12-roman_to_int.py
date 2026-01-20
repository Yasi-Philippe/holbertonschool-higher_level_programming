#!/usr/bin/python3
def roman_to_int(roman_string):
    my_dict = {"I": 1,
               "V": 5,
               "X": 10,
               "L": 50,
               "C": 100,
               "D": 500,
               "M": 1000}
    if len(roman_string) == 1:
        return my_dict[roman_string]
    num = 0
    for i in range(1, len(roman_string)):
        if my_dict[roman_string[i]] <= my_dict[roman_string[i - 1]]:
            num += my_dict[roman_string[i - 1]]
        else:
            num -= my_dict[roman_string[i - 1]]
    if my_dict[roman_string[-1]] <= my_dict[roman_string[-2]]:
        num += my_dict[roman_string[-1]]
    else:
        num += my_dict[roman_string[-1]]
    return num
