# -*- coding:utf-8 -*-
# """
# python --version
# Python 3.6.5 :: Anaconda custom (64-bit)
# """

# #可以在交互环境中看到tim peter撰写的python之禅
# import this
# """
# The Zen of Python, by Tim Peters
#
# Beautiful is better than ugly.
# Explicit is better than implicit.
# Simple is better than complex.
# Complex is better than complicated.
# Flat is better than nested.
# Sparse is better than dense.
# Readability counts.
# Special cases aren't special enough to break the rules.
# Although practicality beats purity.
# Errors should never pass silently.
# Unless explicitly silenced.
# In the face of ambiguity, refuse the temptation to guess.
# There should be one-- and preferably only one --obvious way to do it.
# Although that way may not be obvious at first unless you're Dutch.
# Now is better than never.
# Although never is often better than *right* now.
# If the implementation is hard to explain, it's a bad idea.
# If the implementation is easy to explain, it may be a good idea.
# Namespaces are one honking great idea -- let's do more of those!
#
# 漂亮好过丑陋
# 清晰好过晦涩
# 简单好过复杂
# 复杂好过错综复杂
# 扁平好过嵌套
# 稀疏好过密集
# 可读性很重要
# 特列也不可以特殊到违反到这些规则
# （可行性打败纯洁性）但现实往往没有那么完美
# 异常不应该被静默处理
# （除非明确”要求“静默）除非你喜欢如此
# 遇到模棱两可的情况，拒绝胡乱猜测
# 肯定有一种且唯一的最佳解决方案
# 尽管这种方式没那么显而易见，因为你不是那个荷兰人，（python之父 Guido）
# 现在开始做好过不做
# 不做好过盲目去做
# 如果一个实现方案难于理解，那么不是一个好方案
# 如果一个实现方案易于理解，那么很可能式一个好方案
# 命名空间好主意，我们应该多加利用（honking 鸣喇叭）
# """


# #学习使用turtle在屏幕上绘制图形
# import turtle
#
# # turtle.pensize(4)
# # turtle.pencolor('red')
# #箭头颜色，笔画颜色，笔划大小
# turtle.pen(fillcolor='white', pencolor='red', pensize=4)
#
# #顺时针画一个100*100的正方形
# turtle.forward(100)
# turtle.right(90)
# turtle.forward(100)
# turtle.right(90)
# turtle.forward(100)
# turtle.right(90)
# turtle.forward(100)
#
# turtle.mainloop()
# #---------------------------------------------------------------------------------------------------------------------


#变量和类型
# """
# 在程序设计中，变量是一种存储数据的载体，计算机中的变量是实际的数据或者说
# 是存储器中存储数据的一块内存空间，值可以被读取和修改。
# 数据类型很多，不同的数据需要定义不同的存储类型
# python数据类型很多，也允许自己定义新的数据类型
# 整形：int，支持2，8，10，16进制
# 浮点型：小数，数学写法:123.456, 科学计数法：1.23456e2
# 字符串型：'hello', "hello"
# 布尔型：True，False
# 复数型：3+5j
#
# 命名：
# 硬性规则：
# 变量名由字母（广义的Unicode字符，不包括特殊字符）、数字和下划线构成，数字不能开头。
# 大小写敏感（大写的a和小写的A是两个不同的变量）。
# 不要跟关键字（有特殊含义的单词，后面会讲到）和系统保留字（如函数、模块等的名字）冲突。
# PEP 8要求：一个编程规范，一些使程序更具可读性的建议
# 用小写字母拼写，多个单词用下划线连接。
# 受保护的实例属性用单个下划线开头
# 私有的实例属性用两个下划线开头
# 命名要见名知意
# 从下面开始的代码规范性比较强
# """


# """
# 使用变量保存数据并进行算术运算
#
# Version：0.1
# Author：林忠凯
# """
#
#
# a = 123
# b = 321
# print(a + b)
# print(a - b)
# print(a * b)
# print(a / b)
# print(a // b)       # 取整除 结果123
# print(a % b)        # 取模 结果0
# print(a ** b)       # 幂运算 123的321次方


# """
# 使用input()函数获取键盘输入
# 使用int进行类型转换
# 用占位符格式化输出的字符串
#
# Version：0.1
# Author：林忠凯
# """
#
# a = int(input('a = '))
# b = int(input('b = '))
# print('%d + %d = %d' % (a, b, a + b))
# print('%d + %d = %f' % (a, b, a / b))


# """
# 类型转换
#
# Version：0.1
# Author：林忠凯
# """
#
# a = 500
# b = 'l'
#
# print(type(a),type(b))
# print(type(str(a)))
# print(chr(a).encode('utf-8'))       # chr()将整数转换成该编码对应的字符串（一个字符）
# print(ord(b))                       # 和chr()反过来



# flag = 3 > 1
# print(flag is True)



# """
# 华氏温度转摄氏温度
# 输入圆的半径计算周长和面积
# 判断输入年份是不是闰年
#
# Version：0.1
# Author：林忠凯
# """

# import math

# Fahrenheit = float(input('Fahrenheit:'))
# Celsius= (Fahrenheit - 32) / 1.8
# print('%.1f华氏度 = %.1f摄氏度' % (Fahrenheit, Celsius))



# radius = float(input('please input radius: '))
# perimeter = 2 * math.pi *radius
# area = math.pi * radius ** 2
# print('perimeter: %.3f' % perimeter)
# print('area : %.3f' % area)



# year = int(input("please input year："))
# is_leap = (year % 4 ==0 and
#            year % 100 == 0 or
#            year % 400 ==0)
# print('%d是闰年?'% year, is_leap)
#-----------------------------------------------------------------------------------------------------------------------


# """
# 分支结构（尽量使用扁平化的结构）
# 用户身份结构
# 分段函数求值
#
# """
#
# # username = input("请输入用户名：")
# # password = input("请输入用户密码：")
# #
# # if username=='lzk' and password == 'lzk':
# #     print("欢迎你，%s" % username)
# # else:
# #     print("用户名或者密码出错")
#
# x = float(input("x = "))
# if x > 1:
#     y = 3 * x - 5
# elif x < -1:
#     y = 5 * x + 3
# else:
#     y = x + 2
#
# print("f(%.2f) = %.2f" % (x, y))



# """
# 英制单位英寸和公制单位厘米互换
# 掷骰子决定做什么
# 百分制转换等级制
# 输入三边如果能构成三角形就计算周长和面积
# abs()函数取绝对值
#
# """

# value = float(input("请输入长度："))
# unit = input("请输入单位：")
# if unit == 'in' or unit == '英寸':
#     conver_value = value * 2.54
#     print('%f英寸 = %f厘米' % (value, conver_value))
# elif unit == 'cm' or unit == '厘米':
#     conver_value = value / 2.54
#     print('%f厘米 = %f英寸' % (value, conver_value))
# else:
#     print('请输入有效单位')



# from random import randint      # 导入产生随机数的库
#
# face = randint(1, 6)            # 产生1-6之间的一个数
#
# if face == 1:
#     result = 'song'
# elif face ==2:
#     result = 'dance'
# elif face == 3:
#     result = 'fuck'
# else:
#     result = 'nothing'
#
# print(result)


# score = float(input("请输入你的成绩："))
#
# if score >= 90:
#     grade = 'A'
# elif score >= 80:
#     grade = 'B'
# elif score >= 70:
#     grade = 'C'
# elif score >= 60:
#     grade = 'D'
# else:
#     grade = 'F'
# print('对应的等级是：', grade)


# import math
#
# a = float(input('a = '))
# b = float(input('b = '))
# c = float(input('c = '))
# if a + b > c and b + c > a and a + c > b:
#     print("周长是：", a + b + c)
#     p = (a + b + c) / 2
#     area = math.sqrt(p * (p - a) * (p - b) * (p - c))
#     print("面积是：", area)
# else:
#     print("无法构成三角形的三边")

# print(abs(-0))
#-----------------------------------------------------------------------------------------------------------------------

#0-100
# for x in range(101):
#     print(x)
#步长为2
# for x in range(0, 101,2):
#     print(x)


# """
# 猜字游戏
# """
# from random import randint
#
# answer = randint(1, 100)
# counter = 0
#
# while True:
#     counter += 1
#     number = int(input("请输入："))
#     if number < answer:
#         print("大一点")
#     elif number > answer:
#         print("小一点")
#     else:
#         print('你猜对了')
#         break
# print('你总共用了几次：', counter)

# """
# 99乘法表
# """
# for i in range(1, 10):
#     for j in range(1, i + 1):
#         print('%d*%d=%d' % (i, j, i * j), end='\t')
#     print()


# """
# 判断正整数是不是素数
# """
# from math import sqrt
#
# num = int(input('请输入一个正整数：'))
# end = int(sqrt(num))
# is_prime = True
#
# for x in range(2, end + 1):
#     if num % x ==0:
#         is_prime = False
#         break
#
# if is_prime and num != 1:
#     print('%d是素数' % num)
# else:
#     print('%d不是素数' % num)

# """
# 两个正整数计算最大公约数和最小公倍数
# """
#
# x = int(input("x = "))
# y = int(input("y = "))
#
# if x > y:
#     x , y =  y, x
#
# for factor in range(x, 0, -1):
#     if x % factor == 0 and y % factor == 0:
#         print('%d和%d的最大公约数是%d' % (x, y, factor))
#         print('%d和%d的最小公倍数为%d' % (x, y, x * y //factor))
#         break

# """
# 打印三角形图案
# """
# row = int(input('请输入行数：'))
#
# for i in range(row):
#     for _ in range(i + 1):
#         print('*', end = '')
#     print()     # 自动打出回车
#
# for i in range(row):
#     for j in range(row):
#         if j < row - i - 1:
#             print(' ', end='')
#         else:
#             print('*', end='')
#     print()
#
# for i in range(row):
#     for _ in range(row - i - 1):
#         print(' ', end='')
#     for _ in range(2 * i -1):
#         print('*', end='')
#     print()
#-----------------------------------------------------------------------------------------------------------------------

# """
# 水仙花数
# """
# for num in range(100,1000):
#     num_bai = num // 100
#     num_shi = (num % 100) // 10
#     num_ge = num % 10
#
#     # print(num_ge, num_shi, num_bai)
#
#     if num_ge ** 3 + num_shi ** 3 + num_bai ** 3 == num:
#
#         print('%d数是个水仙花数' % num)
#     else:
#         pass


# """
# 完备数
# """
#
# for num in range(1, 1000):
#     sum_factor = 0
#     for i in range(1, num):
#         if num % i == 0:
#             sum_factor += i
#         else:
#             pass
#     if sum_factor == num:
#         print('%d是个完美数' % num)
#     else:
#         pass


# """
# 百鸡百钱
# 鸡翁一值钱五，鸡母一值钱三，鸡雏三值钱一。
# 百钱买百鸡，问鸡翁、鸡母、鸡雏各几何？
# """
# for num_cock in range(100):
#     for num_hen in range(100):
#         if 14*num_cock + 8*num_hen -200 == 0 and \
#                 100-num_cock-num_hen >= 0:
#             print('公鸡{}只，母鸡{}只，雏鸡{}只'
#                   .format(num_cock, num_hen, (100-num_cock-num_hen)))

# """
# 斐波那契数列
# """
# 
# a=0
# b=1
# for _ in range(20):
#     a, b=b, a+b
#     print(a,end=' ')


# """
# graps赌博游戏
# """
# from random import randint
#
#
# money = 1000
# gamestart = 'init'
# continue_or_not = 'init'
# while True:
#     if gamestart != 'qq':
#         gamestart = input('任意键游戏开始, q退出：')
#         if gamestart != 'q':
#             print('游戏开始')
#             print('你目前拥有的资产是：', money)
#             debt = int(input('请下注：'))
#             while True:
#                 if 0 < debt < money:
#                     result_first = randint(1, 6) + randint(1, 6)
#                     print('第一次结果：', result_first)
#                     if result_first == 7 or result_first == 11:
#                         print('你赢了')
#                         money = money + debt
#                     elif result_first == 2 or result_first == 3 or result_first == 12:
#                         print('你输了')
#                         money = money - debt
#                     else:
#                         result_second = randint(1, 6)
#                         print('第二次结果：', result_second)
#                         if result_second == result_first:
#                             print('你赢了')
#                             money = money + debt
#                         elif result_second == 7:
#                             print('你输了')
#                             money = money - debt
#                         else:
#                             print('平局')
#                     continue_or_not = input('任意键继续，q退出当前轮数， qq退出游戏')
#                     if continue_or_not == 'q':
#                         break
#                     elif continue_or_not == 'qq':
#                         gamestart = 'qq'
#                         break
#                     else:
#                         print('你目前拥有的资产是：', money)
#                         continue
#                 else:
#                     print('下注金额有问题')
#         else:
#             print('游戏结束')
#             break
#     else:
#         print('游戏结束')
#         break










