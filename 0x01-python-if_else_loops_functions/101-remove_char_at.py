#!/usr/bin/python3
def remove_char_at(str, n):
    tmp_str = ""
    if n < 0:
        return str
    for i in range(0, len(str)):
        if i != n:
            tmp_str += str[i]
    return tmp_str
