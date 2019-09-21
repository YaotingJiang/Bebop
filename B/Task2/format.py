import sys
from builtins import isinstance
from json import JSONDecoder, JSONDecodeError


def extract_json(json_string):
    results = []
    decoder = JSONDecoder()
    while json_string != '':
        json_string = json_string.lstrip()
        try:
            json_obj, end_index = decoder.raw_decode(json_string)
        except JSONDecodeError:
            raise
        else:
            if not isinstance(json_obj, bool or int or float) and json_obj is not None:
                results.append(json_obj)
            json_string = json_string[end_index+1:]

    return results


if __name__ == "__main__":
    buffer = ''

    for line in sys.stdin:
        buffer += line

    for obj in extract_json(buffer):
        print(obj)