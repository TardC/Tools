#!usr/bin/env python
# coding: utf-8

"""
Caesar password program
Author: TardC
Date: 2017/06/05 22:02
"""

from string import ascii_lowercase


def init():
    print '------Caesar password------'
    text = raw_input('Input text: ')

    return text


def main():
    text = init()
    for i in xrange(1, 26):  # 移位1,2,...,25
        offset_text = []
        for j in text:
            offset_text.append(ascii_lowercase[(ascii_lowercase.index(j) + i) % 26])
        print i, 'offset:', ''.join(offset_text), ''.join(offset_text).upper()


if __name__ == '__main__':
    main()
