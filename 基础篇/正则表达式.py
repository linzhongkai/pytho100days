# -*- coding:utf-8 -*-
# """
# 验证输入用户名和qq号是否有效并给出相对应的提示信息
# 要求：用户名必须由字母数字或下划线构成且长度在6~20个字符之间，
# qq号是5~12的数字且首位不能是0
# """
# import re
#
# def main():
#     while True:
#         username = input('请输入用户名：')
#         qq = input('请输入qq号：')
#         #match函数的第一个参数是正则表达式字符串或正则表达式对象
#         #第二个参数是要跟正则表达式做匹配的字符串对象
#         #r表示的是原始字符串的意思
#         m1 = re.match(r'^[0-9a-zA-Z_]{6,20}$', username)
#         if not m1:
#             print('请输入有效的用户名.')
#
#         m2 = re.match(r'^[1-9]\d{4,11}$',qq)
#         if not m2:
#             print('请输入有效的qq号.')
#
#         if m1 and m2:
#             print('你输入的信息是有效的.')
#             break
#
# if __name__ == '__main__':
#     main()


"""
从一段文字提取国内手机号码
"""

import re

def main():
    # sentence = '''
    # 重要的事情说8130123456789遍，我的手机号是13512346789这个靓号，
    # 不是15600998765，也是110或119，王大锤的手机号才是15600998765。
    # '''
    # pattern = re.compile(r'(?<=\D)1[34578]\d{9}(?=\D)')
    # mylist = re.findall(pattern, sentence)
    # print(mylist)
    # print('华丽的分割线'.center(40, '-'))
    # #通过迭代器去除匹配对象并获得匹配的内容
    # for temp in pattern.finditer(sentence):
    #     # print(temp)
    #     print(temp.group(), end=' ')
    # print()
    # print('华丽的分割线'.center(40, '-'))
    # m = pattern.search(sentence)
    # print(m)
    # while m:
    #     print(m.group(), end=' ')
    #     #m.end给出下次匹配的起始位置
    #     m = pattern.search(sentence, m.end())
    # print()

    # #替换不良内容：
    # sentence = '你丫是傻叉吗? 我操你大爷的. Fuck you. 你就是一坨SHIT'
    # #IGNORECASE不区分大小写
    # purified = re.sub('[操肏艹草]|fuck|shit|傻[比屄逼吊屌]|煞笔',
    #                   '*', sentence, flags=re.IGNORECASE)
    # print(purified)

    #拆分长字符串
    poem = '床前明月光，疑是地上霜。举头望明月，低头思故乡。'
    sentence_list = re.split(r'[,.，。]', poem)
    print(sentence_list)
    while '' in sentence_list:
        sentence_list.remove('')
    print(sentence_list)

if __name__ == '__main__':
    main()