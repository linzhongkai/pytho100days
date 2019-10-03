# -*- coding:utf-8 -*-
import os
import time
from math import sqrt
import json

# path1 = os.path.abspath('.')
# path2 = os.path.abspath('..')
# print(path1,path2)

def is_prime(n):
    #条件为True正常执行，False触发异常
    assert n > 0
    for factor in range(2, int(sqrt(n)) + 1):
        if n % factor == 0:
            return False
    return True if n != 1 else False

def clone_img(origin, copy):
    #实现程序复制的功能
    try:
        with open(origin, 'rb') as fs1:
            data = fs1.read()
            print(type(data))
        with open(copy, 'wb') as fs2:
            fs2.write(data)
    except FileNotFoundError as e:
        print('指定文件无法打开')
    except IOError as e:
        print('读写文件时出现错误')
    print('程序结束')


def main():
    # f = None
    # try:
    #     with open(r'../readme.txt', 'r', encoding='utf-8') as f:
    #         print(f.read())
    #         # f.close()
    # except FileNotFoundError:
    #     print('无法打开指定文件')
    # except LookupError:
    #     print('指定了未知编码')
    # except UnicodeDecodeError:
    #     print('读取文件时解码错误')
    #无论程序异常还是正常都会被执行到
    #即使使用sys模块中的exit()函数都会被执行，SystemExit异常
    # finally:
    #     if f:
    #         f.close()

    # #通过for-in循环逐行读取
    # with open('../readme.txt', mode='r', encoding='utf-8') as f:
    #     for line in f:
    #         print(line, end='')
    #         time.sleep(0.5)

    # #读取文件到列表
    # with open('../readme.txt', mode='r', encoding='utf-8') as f:
    #     lines = f.readlines()
    # print(lines)


    # filenames = ['a.txt', 'b.txt', 'c.txt']
    # fs_list = []
    # try:
    #     for filename in filenames:
    #         fs_list.append(open(filename, 'w', encoding='utf-8'))
    #     # print(fs_list)
    #     for number in range(1, 10000):
    #         if is_prime(number):
    #             fs_list[0].write(str(number) + '\n')
    #         elif number < 1000:
    #             fs_list[1].write(str(number) + '\n')
    #         else:
    #             fs_list[2].write(str(number) + '\n')
    # except IOError as ex:
    #     print(ex)
    #     print('写入文件发生错误')
    # finally:
    #     for fs in fs_list:
    #         fs.close()
    # print('操作完成')

    #json数据
    mydict={
        'name': 'lzk',
        'age':22,
        'friend':['cpg','ljj','xwh','mjh'],
        'cars':[
            {'brand': 'BMW', 'max_speed':220},
            {'brand': 'Benz', 'max_speed':180}
        ]
    }
    try:
        with open('data.json', 'w', encoding='utf-8') as fs:
            json.dump(mydict, fs)
    except IOError as e:
        print(e)
    print('保存数据完成')



if __name__ == '__main__':
    main()



