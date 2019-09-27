# -*- coding:utf-8 -*-
import os
import time
import random

def add(*args):
    """
    :param args:任意个数参数
    :return: 参数之和
    """
    sum = 0
    for val in args:
        sum += val
    return sum

def gcd(x, y):
    """
    求计算参数的最大公约数
    :param x:计算参数
    :param y: 计算参数
    :return: 最大公约数
    """
    (x, y) = (y, x) if x > y else (x, y)
    for factor in range(x, 0, -1):
        if x % factor == 0 and y % factor == 0:
            return factor


def lcm(x, y):
    """
    求计算参数的最小公倍数
    :param x:
    :param y:
    :return:
    """
    return x * y // gcd(x, y)


def verifycode(length):
    """
    产生验证码
    :param length:验证码长度
    :return: 验证码结果
    """
    all_chars = '0123456789' \
                'abcdefghijklmnopqrstuvwxyz' \
                'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    code = ''
    # print(len(all_chars))
    for i in range(length):
        index = random.randint(0, len(all_chars)-1)
        code += all_chars[index]
    return code


def max2(content):
    """
    返回传入的列表中最大和第二大的元素的值
    :param content:
    :return:
    """
    # if content[0] > content[1]:
    #     max_num = content[0]
    #     sec_num = content[1]
    # else:
    #     max_num = content[1]
    #     sec_num = content[0]
    max_num, sec_num = (content[0], content[1]) if content[0] > content[1] \
        else (content[1], content[0])
    for i in range(2, len(content)):
        if max_num < content[i]:
            sec_num = max_num
            max_num = content[i]
        elif sec_num < content[i]:
            sec_num = content[i]
        else:
            pass
    return max_num, sec_num


"""
指定的年月日是这一年的第几天
"""
def is_lead_year(year):
    return year % 4 == 0 and year % 100 != 0 or year % 400 == 0

def which_day(year, month, day):
    days_of_month = [
        [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31],
        [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    ][is_lead_year(year)]   # 注意这一块的用法
    day_num = 0

    for index in range(month-1):
        day_num += days_of_month[index]
    return day_num + day



def Factorial(n):
    """
    求阶乘
    :param n:
    :return:
    """
    multi = 1
    for i in range(1, n+1):
        multi = i*multi
    # print(multi)
    return multi

def yanhui_triangle(n):
    """
    打印杨辉三角
    :param n: 阶数
    :return: 无返回
    """
    for i in range(1, n+1):
        for m in range(1, i+1):
            num = int(Factorial(i-1)/(Factorial(m-1)*Factorial(i-m)))
            print(num, end='\t')
        print()

    #另一种实现方式
    num = int(input('Number of rows: '))
    yh = [[]] * num
    for row in range(len(yh)):
        yh[row] = [None] * (row + 1)
        for col in range(len(yh[row])):
            if col == 0 or col == row:
                yh[row][col] = 1
            else:
                yh[row][col] = yh[row - 1][col] + yh[row - 1][col - 1]
            print(yh[row][col], end='\t')
        print()

def lcuky_christian():
    """
    幸运的基督徒：
    有15个基督徒和15个非基督徒在海上遇险，为了能让一部分人活下来不得不将其中15个人扔到海里面去，
    有个人想了个办法就是大家围成一个圈，由某个人开始从1报数，报到9的人就扔到海里面，他后面的人接
    着从1开始报数，报到9的人继续扔到海里面，直到扔掉15个人。由于上帝的保佑，15个基督徒都幸免于难
    ，问这些人最开始是怎么站的，哪些位置是基督徒哪些位置是非基督徒。
    :return: 排序
    """
    people = [True] * 30

    counter = 0 #丢掉的人数
    index = 0   # 丢掉的人
    number = 0
    while counter < 15:
        if people[index]:
            number += 1
            if number == 9:
                people[index] = False
                counter += 1
                number = 0
        index += 1
        index %= 30
    for person in people:
        print('基' if person else '非', end=' ' )


def main():

    lcuky_christian()

    #测试enumerate函数
    # try_enumerate = ['linzhongkai', 'xiaolin', 'xiaokai', 'laozhong']
    # enu_list = enumerate(try_enumerate)
    # for val in enu_list:
    #     print(val, end=' ')


if __name__ == '__main__':
    main()

    # n = int(input('你要打印的阶数：'))
    # yanhui_triangle(n)

    # print(which_day(2001, 3, 1))


    # x1, x2 = max2([1, 2, 3, 1090, 19, 109, 90, 10])
    # print(x1, x2)


    # code = verifycode(4)
    # print(code)
    # verify_num = str(input('请输入验证码：'))
    # if verify_num != code:
    #     print('输入有误！')
    # else:
    #     print('通过')

    # print(add(1 + 2 + 3))

