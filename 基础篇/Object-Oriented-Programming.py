# -*- coding:utf-8 -*-

# from time import time, localtime, sleep
# from math import sqrt
#
# class Students(object):
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def study(self, course_name):
#         print('%s正在学习%s' %(self.name, course_name))
#
#     def watch_movie(self):
#         if self.age < 18:
#             print('%s只能看喜羊羊' % self.name)
#         else:
#             print('%s正在观看岛国爱情动作片' % self.name)
#
#
# class Test(object):
#     def __init__(self, foo):
#         self.__foo = foo
#
#     def __bar(self):
#         print(self.__foo)
#         print('__bar')
#
#
# class Clock(object):
#     def __init__(self, hour=0, minute=0,second=0):
#         """
#         初始化方法
#         :param hour:时
#         :param minute:分
#         :param second: 秒
#         """
#         self._hour = hour
#         self._minute = minute
#         self._second =second
#     @classmethod
#     def now(cls):
#         ctime = localtime(time())
#         return cls(ctime.tm_hour, ctime.tm_min,
#                    ctime.tm_sec)
#
#     def run(self):
#         """走字"""
#         self._second += 1
#         if self._second == 60:
#             self._second = 0
#             self._minute += 1
#             if self._minute == 60:
#                 self._minute = 0
#                 self._hour += 1
#                 if self._hour == 24:
#                     self._hour = 0
#
#     def show(self):
#         """显示时间"""
#         return '%02d:%02d:%02d' % \
#                (self._hour, self._minute, self._second)
#
# class Point(object):
#     def __init__(self, x=0, y=0):
#         """
#         初始化方法
#         :param x:横坐标
#         :param y: 纵坐标
#         """
#         self.x = x
#         self.y = y
#
#     def move_to(self, x, y):
#         """
#         移动到指定位置
#         :param x: 新的横坐标
#         :param y: 新的纵坐标
#         """
#         self.x = x
#         self.y = y
#
#     def move_by(self, dx, dy):
#         """
#         移动增量
#         :param dx: 横坐标增量
#         :param dy: 纵坐标增量
#         """
#         self.x += dx
#         self.y += dy
#
#     def distance_to(self, other):
#         """
#         计算到另一个点的距离
#         :param other: 另一个点
#         """
#         distance = sqrt((self.x - other.x)**2
#                         + (self.y - other.y)**2)
#         return distance
#
#     def __str__(self):
#         return '(%s, %s)' % (str(self.x), str(self.y))
#
# class Person():
#     #限制Person对象只能绑定_name等属性
#     __slots__ = ('_name', '_age', '_gender')
#
#
#     def __init__(self, name, age):
#         self._name = name
#         self._age = age
#
#     @property
#     def information(self):
#         return self._name, self._age
#
#
#     @information.setter
#     def informatioon(self,name, age):
#         self._name = name
#         self._age = age
#
# class lzk(Person):
#     def __init__(self, name, age, grade):
#         super().__init__(name, age)
#         self._grade = grade
#
#     @property
#     def grade(self):
#         return self._grade
#
#     @grade.setter
#     def grade(self, grade):
#         self._grade = grade
#
#
# class Triangle(object):
#     def __init__(self, a, b, c):
#         self._a = a
#         self._b = b
#         self._c = c
#
#     @staticmethod
#     def is_valid(a, b, c):
#         return a+b>c and a+c>b and b+c>a
#
#     def perimeter(self):
#         return self._a+self._b+self._c
#
#     def area(self):
#         half = self.perimeter()/2
#         return sqrt(half*(half-self._a)*
#                     (half-self._b)*(half-self._c))
#
# def main():
#
#
#
#     # xiaolin = lzk('林忠凯', 22, 120)
#     # print(xiaolin.information)
#     # print(xiaolin.grade)
#
#
#     # #通过类方法创建对象并获取时间
#     # clock = Clock.now()
#     # while True:
#     #     print(clock.show())
#     #     sleep(1)
#     #     clock.run()
#
#
#     # a,b,c = 3,4,5
#     # #静态方法和类方法都是通过给类发消息来调用的
#     # if Triangle.is_valid(a,b,c):
#     #     t=Triangle(a,b,c)
#     #     print(t.perimeter())
#     #     #也可以通过给类发消息来调用对象方法但是要传参
#     #     print(Triangle.perimeter(t))
#     #     print(t.area())
#     # else:
#     #     print('无法构成三角形')
#
#     #测试__slots__()
#     # person = Person('lzk')
#     # print(person._name)
#     # person._age = 22
#     # person._gender = 'man'
#     # person._gay = True
#
#
#     #测试@property
#     # man = Person('lzk')
#     # print(man.name)
#     # man.name='xiaolin'
#     # print(man.name)
#
#
#     # p1 = Point(3, 5)
#     # p2 = Point()
#     # print(p1)
#     # print(p2)
#     # p2.move_by(-1, 2)
#     # print(p2)
#     # print(p1.distance_to(p2))
#     # print(p2.distance_to(p1))
#
#
#     # clock = Clock(23, 59, 28)
#     # while True:
#     #     print(clock.show())
#     #     time.sleep(1)
#     #     clock.run()
#
#
#     #事实上如果你知道更换名字的规则仍然可以访问到它们
#     #使用单下划线暗喻属性和方法是受保护的，但是实际上外面是可以访问的
#     # test = Test('try')
#     # test._Test__bar()
#     # print(test._Test__foo)
#
#
#     # test = Test('try')
#     # test.__bar()
#     # print(test.__foo)
#
#
#     # stu1 = Students('lzk', 22)
#     # stu1.study('python')
#     # stu1.watch_movie()
#
#
# if __name__ == '__main__':
#     main()



# from abc import ABCMeta, abstractmethod
#
# class Pet(object, metaclass=ABCMeta):
#     """宠物"""
#     def __init__(self, nickname):
#         self._nickname = nickname
#
#     @abstractmethod
#     def make_vioce(self):
#         pass
#
# class Dog(Pet):
#     def make_vioce(self):
#         print('%s:w w w...' % self._nickname)
#
# class Cat(Pet):
#     def make_vioce(self):
#         print('%s: m m m...' % self._nickname)
#
# def main():
#     """
#     当我们在main函数中调用该方法时，
#     这个方法就表现出了多态行为（同样的方法做了不同的事情）。
#     :return:
#     """
#     pets = [Dog('旺财'), Cat('凯蒂')]
#     for pet in pets:
#         pet.make_vioce()
#
# if __name__ == '__main__':
#     main()



# #测试抽象基类的两种方法
#
# from abc import ABCMeta, abstractmethod
#
# class Baseclass(object, metaclass=ABCMeta):
#
#     def __init__(self, test):
#         self._test = test
#
#     @property
#     def test(self):
#         return self._test
#     @test.setter
#     def test(self, test):
#         self._test = test
#
#     @abstractmethod
#     def func_1(self):
#         pass
#
#     @abstractmethod
#     def fun_2(self):
#         pass
#
# # class_1 = Baseclass()
# #TypeError: Can't instantiate abstract class Baseclass with abstract methods fun_2, func_1
#
# class Subclass(Baseclass):
#
#     def func_1(self):
#         print('函数1')
#
#     def fun_2(self):
#         print('函数2')
#
# example1 = Subclass('测试')
# #TypeError: Can't instantiate abstract class subclass with abstract methods fun_2
# example1.func_1()
# example1.fun_2()
#
# class Regclass(object):
#     @staticmethod
#     def func_1(self):
#         print('注册类的函数1')
#
#
#
# for sub in Baseclass.__subclasses__():
#     # 由內定__subclasses__()方法查看含有那些子類別
#     print('子类有：%s' % sub.__name__ )
#
# print(str(issubclass(Regclass, Baseclass)))
# print(type(issubclass(Regclass, Baseclass)))
# print(str(isinstance(Regclass(),Baseclass)))
#
# print(str(issubclass(Subclass, Baseclass)))
# print(str(isinstance(Subclass, Baseclass)))
#
# Baseclass.register(Regclass)
#
# print(str(issubclass(Regclass, Baseclass)))
# print(str(isinstance(Regclass(), Baseclass)))



# from abc import ABCMeta, abstractmethod
# from random import randint, randrange
#
# class Fighter(object, metaclass=ABCMeta):
#     """战斗者"""
#     __slots__ = ('_name', '_hp')
#
#     def __init__(self, name, hp):
#         self._name = name
#         self._hp = hp
#
#     @property
#     def name(self):
#         return self._name
#     @property
#     def hp(self):
#         return self._hp
#     @hp.setter
#     def hp(self, hp):
#         self._hp = hp
#
#     @property
#     def alive(self):
#         return self._hp>0
#
#     @abstractmethod
#     def attack(self, other):
#         """
#         攻击
#         :param other:被攻击的对象
#         :return: 无
#         """
#         pass
#
# class Ultraman(Fighter):
#     """奥特曼"""
#     __slots__ = ('_name', '_hp', '_mp')
#
#     def __init__(self, name, hp, mp):
#         """
#         初始化方法
#         :param name:
#         :param hp:
#         :param mp:魔法值
#         """
#         super().__init__(name, hp)
#         self._mp = mp
#
#     def attack(self, other):
#         other.hp -= randint(15, 25)
#
#     def huge_attack(self, other):
#         """
#         究极必杀技(打掉对方至少50点或四分之三的血)
#         :param other:被攻击的对象
#         :return:使用成功返回True，否则False
#         """
#         if self._mp > 50:
#             self._mp -= 50
#             injury = other.hp*3 // 4
#             injury = injury if injury > 50 else 50
#             other.hp -= injury
#             return True
#         else:
#             self.attack(other)
#             return False
#     def magic_attack(self, others):
#         """
#         魔法攻击
#         :param others:被攻击的群体
#         :return: 成功True，失败False
#         """
#         if self._mp > 20:
#             self._mp -= 20
#             for temp in others:
#                 if temp.alive:
#                     temp.hp -= randint(10, 15)
#             return True
#         else:
#             return False
#
#     def resum(self):
#         """
#         灰度魔法值
#         :return: 恢复的点数
#         """
#         incr_point = randint(1,10)
#         self._mp += incr_point
#         return incr_point
#
#     def __str__(self):
#         return '~~~%s奥特曼~~~\n' % self._name+'生命值：%d\n' % self._hp +'魔法值：%d\n' % self._mp
#
# class Monster(Fighter):
#     """小怪兽"""
#     __slots__ = ('_name', '_hp')
#
#     # def __init__(self, name, hp):
#     #     super().__init__(name, hp)
#
#     def attack(self, other):
#         other.hp -= randint(10, 20)
#
#     def __str__(self):
#         return '~~~%s小怪兽~~~\n' % self._name +\
#             '生命值：%d\n' % self._hp
#
#
# def is_any_live(monsters):
#     for monster in monsters:
#         if monster.alive > 0:
#             return True
#     return False
#
# def select_alive_one(monsters):
#     monsters_len = len(monsters)
#     while True:
#         index = randrange(monsters_len)
#         monster = monsters[index]
#         if monster.alive > 0:
#             return monster
#
# def dispaly_info(ultramen, monsters):
#     """显示奥特曼和小怪兽的信息"""
#     print(ultramen)
#     for monster in monsters:
#         print(monster, end=' ')
#
# def main():
#     u = Ultraman('林忠凯', hp=800, mp=120)
#     m1 = Monster('罗进杰', hp=250)
#     m2 = Monster('陈鹏贵', hp=500)
#     m3 = Monster('徐伟豪', hp=750)
#     ms = [m1, m2, m3]
#     fight_round = 1
#     while u.alive and is_any_live(ms):
#         print('=======第%02d回合=======' % fight_round)
#         m = select_alive_one(ms)
#         skill = randint(1, 10)
#         if skill <= 6:
#             print('%s使用普通攻击打了%s.' % (u.name, m.name))
#             u.attack(m)
#             print('%s的魔法值恢复了%d点' % (u.name, u.resum()))
#         elif skill <= 9:
#             if u.magic_attack(ms):
#                 print('%s使用了魔法攻击.' % u.name)
#             else:
#                 print('%s使用魔法失败' % u.name)
#         else:
#             if u.huge_attack(m):
#                 print('%s使用究极必杀技虐了%s.' % (u.name, m.name))
#             else:
#                 print('%s使用普通攻击打了%s.' % (u.name, m.name))
#                 print('%s的魔法值恢复了%d点.' % (u.name, u.resum()))
#         if m.alive > 0:
#             print('%s回击了%s.' % (m.name, u.name))
#             m.attack(u)
#         dispaly_info(u, ms)
#         fight_round += 1
#     print('\n=======战斗结束=======\n')
#     if u.alive > 0:
#         print('%s奥特曼胜利！' % u.name)
#     else:
#         print('小怪兽胜利！')
#
#
# if __name__ == '__main__':
#     main()


#扑克游戏
"""
[A, 2:10, J, Q, K]
1：发牌前随机选择一名玩家作为庄家
2：从庄家开始随机各发两张牌
"""