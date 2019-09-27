# -*- coding:utf-8 -*-
import time
from math import sqrt

class Students(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def study(self, course_name):
        print('%s正在学习%s' %(self.name, course_name))

    def watch_movie(self):
        if self.age < 18:
            print('%s只能看喜羊羊' % self.name)
        else:
            print('%s正在观看岛国爱情动作片' % self.name)


class Test(object):
    def __init__(self, foo):
        self.__foo = foo

    def __bar(self):
        print(self.__foo)
        print('__bar')


class Clock(object):
    def __init__(self, hour=0, minute=0,second=0):
        """
        初始化方法
        :param hour:时
        :param minute:分
        :param second: 秒
        """
        self._hour = hour
        self._minute = minute
        self._second =second

    def run(self):
        """走字"""
        self._second += 1
        if self._second == 60:
            self._second = 0
            self._minute += 1
            if self._minute == 60:
                self._minute = 0
                self._hour += 1
                if self._hour == 24:
                    self._hour = 0

    def show(self):
        """显示时间"""
        return '%02d:%02d:%02d' % \
               (self._hour, self._minute, self._second)

class Point(object):
    def __init__(self, x=0, y=0):
        """
        初始化方法
        :param x:横坐标
        :param y: 纵坐标
        """
        self.x = x
        self.y = y

    def move_to(self, x, y):
        """
        移动到指定位置
        :param x: 新的横坐标
        :param y: 新的纵坐标
        """
        self.x = x
        self.y = y

    def move_by(self, dx, dy):
        """
        移动增量
        :param dx: 横坐标增量
        :param dy: 纵坐标增量
        """
        self.x += dx
        self.y += dy

    def distance_to(self, other):
        """
        计算到另一个点的距离
        :param other: 另一个点
        """
        distance = sqrt((self.x - other.x)**2
                        + (self.y - other.y)**2)
        return distance

    def __str__(self):
        return '(%s, %s)' % (str(self.x), str(self.y))

def main():

    p1 = Point(3, 5)
    p2 = Point()
    print(p1)
    print(p2)
    p2.move_by(-1, 2)
    print(p2)
    print(p1.distance_to(p2))
    print(p2.distance_to(p1))

    # clock = Clock(23, 59, 28)
    # while True:
    #     print(clock.show())
    #     time.sleep(1)
    #     clock.run()


    #事实上如果你知道更换名字的规则仍然可以访问到它们
    #使用单下划线暗喻属性和方法是受保护的，但是实际上外面是可以访问的
    # test = Test('try')
    # test._Test__bar()
    # print(test._Test__foo)


    # test = Test('try')
    # test.__bar()
    # print(test.__foo)


    # stu1 = Students('lzk', 22)
    # stu1.study('python')
    # stu1.watch_movie()


if __name__ == '__main__':
    main()