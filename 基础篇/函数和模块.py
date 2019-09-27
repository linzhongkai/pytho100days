# -*- coding:utf-8 -*-

import mymodels
from mymodels import add, gcd, lcm
import os


def main():
    """
    字符串的使用和处理
    列表的使用和处理
    :return:
    """
    # test_str = 'hello, world!'
    # #len计算长度
    # print(len(test_str))
    # #首字母大写
    # print(test_str.capitalize())
    # #字符串大写
    # print(test_str.upper())
    # #查找子串的位置
    # print(test_str.find('or'))  # 8
    # print(test_str.find('shit'))    # -1
    # #index函数
    # print(test_str.index('or')) # 8
    # # print(test_str.index('shit')) # valueerror异常
    # #检查字符串是否以指定字符串开头
    # print(test_str.startswith('he'))
    # print(test_str.startswith('He'))
    # #检查字符串是否一指定的字符串结尾
    # print(test_str.endswith('!'))
    # #将字符串以指定的宽度居中并在两侧填充指定的字符
    # print(test_str.center(50, '-'))
    # #靠右/左侧放置，左/右侧填充
    # print(test_str.rjust(50,'-'))
    # print(test_str.ljust(50, '-'))
    # #下标运算
    # print(test_str[0])  # h
    # #切片
    # print(test_str[0:5])    # hello
    # #检查字符串是否由数字构成
    # print(test_str.isdigit())   # False
    # #检查字符串是否由字母构成
    # print(test_str.isalpha())   # False 仅限于纯字母
    # #检查是否由字母和数字构成
    # print(test_str.isalnum()) # False
    # #修改左右两侧空格
    # an_test_str = ' fuck you '
    # print(an_test_str)
    # print(an_test_str.strip())


    # test_list = [1, 3, 5, 7, 100]
    # print(test_list)
    # an_test_list = ['lzk'] * 3
    # print(an_test_list)
    # #计算列表长度
    # print(len(test_list))
    # #下标索引
    # print(test_list[4]) # 100
    # print(test_list[-1])    # 100
    # #修改元数
    # test_list[0] = 0
    # print(test_list) # [0, 3,...]
    # #添加元素
    # test_list.append(101)
    # print(test_list)
    # #删除元素
    # test_list.remove(0)
    # print(test_list)    # [3, 5, 7, 100, 101]
    # del test_list[0]
    # print(test_list)    # [5, 7, 100, 101]
    # #清空列表
    # test_list.clear()
    # print(test_list)    # []


    # #列表切片
    # fruits = ['grape', 'apple', 'stawberry', 'waxberry']  # 葡萄 杨梅
    # fruits += ['pitaya', 'pear', 'mango']    #火龙果 梨
    # for fruit in fruits:
    #     print(fruit.title(), end=' ')
    #     # print(fruit.capitalize(), end='\n')
    # print()
    # #列表切片
    # fruits_part = fruits[0:1]   # grape
    # print(fruits_part)
    # fruits_new = fruits #没有复制列表，只是创建了新的引用
    # print(fruits_new)
    # #通过完整的切片实现复制列表
    # fruits_new = fruits[:]
    # print(fruits_new)
    # #通过反向切片实现倒转后的列表的拷贝
    # fruits_rever = fruits_new[::-1]
    # print(fruits_rever)


    # #列表的排序作用
    # list_sort = ['apple', 'orange', 'zoo', 'people', 'graduate student']
    # list_sorted = sorted(list_sort)
    # print(list_sorted)
    # #反序
    # list_sorted = sorted(list_sort, reverse=True)
    # print(list_sorted)
    # #通过key关键词参数指定按照字符串长度进行排序
    # list_sorted = sorted(list_sort, key=len)
    # print(list_sort)
    # #给列表对象直接发出排序信息，直接在列表对象上进行排序
    # list_sort.sort(reverse=True)
    # print(list_sort)

    #使用列表的生成语法创建列表

    # import sys  # 建议放在开头
    #
    # a_list = [x for x in range(1, 10)]
    # print(a_list)
    # a_list = [x+y for x in 'ABCD' for y in '1234567']
    # print(a_list)
    # a_list = [x ** 2 for x in range(1, 10)]
    # print(a_list)
    # #用这种方式元素已经准备就绪，所以需要耗费较多的内存空间
    # #查看对象占用内存的字节数
    # print(sys.getsizeof(a_list))
    # #创建生成器对象，通过生成器可以获取到数据，但不占用额外的内存空间
    # a_list = (x ** 2 for x in range(1, 10))
    # print(a_list)
    # print(sys.getsizeof(a_list))
    # for val in a_list:
    #     print(val)


#     for val in fib(20):
#         print(val)
#
# #通过yield关键字实现将一个普通函数改造成生成器函数
# #斐波那契额数列生成器函数
# def fib(n):
#     a, b = 0, 1
#     for _ in range(n):
#         a, b=b, a+b
#         yield a


    # #元组的使用
    # #定义元组
    # t = ('林忠凯', 23, True, '广东深圳')
    # # t = ['lzk', 126, True]    # 列表
    # print(t)
    # #获取元素
    # print(t[0].center(50, '*'))
    # #遍历
    # for t_v in t:
    #     print(t_v)
    # print('分割线'.center(50, '-'))
    # #重新赋值
    # # t[0] = '小林'     # TYPEERROR
    # #使用新的元组
    # t = ('小林', 23, True, '广东深圳')
    # print(t)
    # #元组转换成列表
    # mine = list(t)
    # print(mine)
    # #列表转换成元组
    # t = tuple(mine)
    # print(t)


    # #使用集合
    # myset = {1, 2, 3, 3}
    # #不算重复元素
    # print(myset)
    # print(len(myset))
    # another_set = set(range(1,6))
    # print(another_set)
    # #添加元素
    # myset.add(4)
    # myset.add(5)
    # print(myset)
    # another_set.update([6, 7])
    # print(another_set)
    # #删除元素
    # another_set.discard(5)
    # another_set.remove(6)
    # print(another_set)
    # another_set.discard(5)
    # # another_set.remove(5) # 使用remove若元素不存在会触发异常
    # #使用remove的方式可以是：
    # if 5 in another_set:
    #     another_set.remove(5)
    # print(another_set)
    # #遍历集合容器
    # for elem in myset:
    #     print(elem ** 2, end=' ')
    # print()
    # #元组转成集合
    # tuple2set = set((1, 2, 3, 4, 3, 1))
    # print(tuple2set)
    # print(tuple2set.pop())  # 从左边删除
    # print(tuple2set)
    # #集合间的运算
    # print('分割线又来了'.center(50, '-'))
    # print(myset, another_set)
    # print(myset & another_set)  # 交集
    # print(myset.intersection(another_set))
    # print(myset | another_set)  # 并集
    # print(myset.union(another_set))
    # print(myset - another_set)  # 差集
    # print(myset.difference(another_set))
    # print(myset ^ another_set)  # 对称差运算
    # print(myset.symmetric_difference(another_set))
    # #判断子集和超集
    # print(myset <= another_set)
    # print(myset.issubset(another_set))


    # #使用字典，键值对
    # information = {'林忠凯': 22, '小林': '林忠凯', '狗嗨': '罗进杰'}
    # print(information['小林'])
    # print(information[information['小林']])
    # #对字典进行遍历
    # for elem in information:
    #     print('{}--->{}'.format(elem, information[elem]))
    # #更新字典元素
    # information['罗小吊'] = 23
    # information.update(老罗='罗进杰')
    # print(information)
    # print(information.get('老罗'))    #get()也是通过键值对实现的
    # #删除字典中的元素
    # print(information.popitem())
    # print(information.pop('林忠凯', 23))   #通过键来索引
    # print(information)
    # #清空字典
    # print(information.clear())


if __name__ == '__main__':
    main()





