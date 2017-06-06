#!/usr/bin/env python
# coding: utf-8

"""
rot13 program
Author: TardC
date: 2017/06/06 21:20
"""

from string import ascii_letters


def init():
    print '------ROT13------'
    text = raw_input('Input text: ')

    return text


def main():
    lower_letter1 = ascii_letters[:13]
    lower_letter2 = ascii_letters[13:26]
    upper_letter1 = ascii_letters[26:39]
    upper_letter2 = ascii_letters[39:]
    text = init()
    text_rot13 = []
    for c in text:
        if c in lower_letter1:
            text_rot13.append(lower_letter2[lower_letter1.index(c)])
        elif c in lower_letter2:
            text_rot13.append(lower_letter1[lower_letter2.index(c)])
        elif c in upper_letter1:
            text_rot13.append(upper_letter2[upper_letter1.index(c)])
        elif c in upper_letter2:
            text_rot13.append(upper_letter1[upper_letter2.index(c)])
        else:
            text_rot13.append(c)

    print ''.join(text_rot13)


if __name__ == '__main__':
    main()
