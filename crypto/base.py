#!/usr/bin/env python
# coding: utf-8

"""
Base encode and decode program
Author: TardC
Date: 2017/06/06 22:16
"""

import base64


def init():
    prompt = ('------Base64------\n'
              '    [*] Encode\n'
              '    [*] Decode\n'
              'E for Encode or D for Decode')
    print prompt
    choice = raw_input('Input E or D: ')
    text = raw_input('Input text: ')

    return choice, text


def decode(text):
    return base64.b64decode(text)


def encode(text):
    return base64.b64encode(text)


def main():
    choice, text = init()
    if choice.upper() == 'E':
        print encode(text)
    elif choice.upper() == 'D':
        print decode(text)
    else:
        print 'Input Error'


if __name__ == '__main__':
    main()
