#!usr/bin/env python
# coding: utf-8

"""
Fence password encryption and decryption program
Author: TardC
Date: 2017/06/05 21:04

Test case:
THERE IS A CIPHER
2 columns: TEESCPEHRIAIHR
7 columns: TAHCEIRPEHIESR
"""


def init():
    prompt = ('------Fence password------\n'
              '    [*] Encryption\n'
              '    [*] Decryption\n'
              'E for Encryption or D for Decryption')
    # prompt = prompt.decode('utf-8').encode('GBK')  # 控制台是UTF-8编码可删除该行
    print prompt
    choice = raw_input('Input E or D: ')
    text = raw_input('Input text: ')
    text = ''.join(text.split(' '))

    return choice, text
    pass


def encryption(text):
    text_len = len(text)
    for i in xrange(2, text_len):
        if text_len % i == 0:  # 如果i能整除text_len则i栏栅栏密码存在
            cipher = []
            for j in xrange(i):  # 分别得到每栏密码再连接得到最后密码
                cipher.append(text[j::i])
            print i, 'columns:', ''.join(cipher)
            pass
    pass


def decryption(cipher):
    cipher_len = len(cipher)
    for i in xrange(2, cipher_len):
        if cipher_len % i == 0:  # 如果i能整除cipher_len则可能是i栏栅栏密码
            text = []
            tmp = cipher_len / i
            for j in xrange(tmp):  # 将密码分成i组，每次取每组首字母再连接得到最后明文
                text.append(cipher[j::tmp])
            print i, 'columns:', ''.join(text)
            pass
    pass


def main():
    choice, text = init()
    if choice.upper() == 'E':
        encryption(text)
        pass
    elif choice.upper() == 'D':
        decryption(text)
    else:
        print 'Input Error'
    pass


if __name__ == '__main__':
    main()
