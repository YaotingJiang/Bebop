#!/usr/bin/env python3
import sys
import os
import argparse
import json


#
def json_null_number_boolean(list_of_json, total_input):
    a_json = ""
    total_length = len(total_input)
    count = 0
    for i in range(total_length):
        current_char = total_input[i]
        if current_char != " ":
            a_json = a_json + current_char
            count = count + 1
        else:
            break
    rest_input = total_input[count + 1:total_length]
    list_of_json.append(a_json)
    find_the_json(list_of_json, rest_input)


#
def json_string(list_of_json, total_input):
    if is_the_end(total_input):
        return


# Take in a string, return the first found list type
def json_array(list_of_json, total_input):
    if is_the_end(total_input):
        return


# Take in a string, return the first found object type
def json_object(list_of_json, total_input):
    if is_the_end(total_input):
        return


#
def is_the_end(total_input):
    length = len(total_input)
    if length == 0:
        return True
    else:
        return False


# To determine the data type for the next Json
def find_the_json(list_of_json, total_input):
    if is_the_end(total_input):
        return
    first_element = total_input[0]
    if first_element == "\"":
        json_string(list_of_json, total_input)
    elif first_element == "[":
        json_array(list_of_json, total_input)
    elif first_element == "{":
        json_object(list_of_json, total_input)
    else:
        json_null_number_boolean(list_of_json, total_input)


def main():
    argument_list = sys.argv
    length_of_args = len(argument_list) - 1
    if length_of_args != 1:
        print("Missing input")
        # exit()

    # parser = argparse.ArgumentParser()
    # parser.add_argument("-up", action="store_true", default=False)
    # parser.add_argument("-down", action="store_true", default=False)
    # arguments = parser.parse_args(argument_list)

    # null 123 True ”a” ["b",1,2,3] {"this" : "c", "other" : 0}
    #
    dictionary_1 = {"this": "c", "other": 0}
    string_1 = "ab \n c"
    list_1 = ["b", 1, 2, 3]
    list_2 = ["null", "123", "True"]

    total_input = sys.stdin.read()
    new_total = total_input.replace("\n", "")

    list_of_json = []
    find_the_json(list_of_json, new_total)
    print(list_of_json)

    # if arguments.up:
    # sort the values in ascending
    # pass
    # else:
    # sort the values in descending
    # pass


if __name__ == "__main__":
    s = "abc"
    a = """{"this": "ab"}"""
    print(json.loads(a))

    main()
