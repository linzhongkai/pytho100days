# -*- coding:utf-8 -*-
# # """
# # 使用tkinter开发GUI的步骤：
# # 1：导入tkinter模块需要的东西
# # 2：创建一个顶层窗口对象并用来承载整个GUI应用
# # 3：在顶层窗口对象添加GUI组件
# # 4：将GUI组件的功能组织起来
# # 5：进入主事件循环（main loop）
# # """
# import tkinter
# import tkinter.messagebox
#
# def main():
#     flag = True
#
#     #修改标签文字
#     def change_label_text():
#         nonlocal flag
#         flag = not flag
#         color, msg = ('red', 'hello, 树先生!') \
#             if flag else ('blue', 'fuck you world!')
#         label.config(text=msg, fg=color)
#
#     def confirm_to_quit():
#         if tkinter.messagebox.askokcancel('温馨提示', '确定要退出吗？'):
#             top.quit()
#
#     #创建顶层窗口
#     top = tkinter.Tk()
#     #设置顶层窗口的大小
#     top.geometry('240x160')
#     #设置窗口标题
#     top.title('小游戏')
#     #创建标签对象并添加到顶层窗口
#     label = tkinter.Label(top, text='hello, world!',
#                           font = 'Arial -32', fg = 'red')
#     label.pack(expand=1)
#     #创建一个装按钮的容器
#     panel = tkinter.Frame(top)
#     #创建按钮对象，指定添加到哪个容器中，通过command参数绑定事件回调对象
#     button1 = tkinter.Button(panel, text='修改', command=change_label_text)
#     button1.pack(side='left')
#     button2 = tkinter.Button(panel, text='退出', command = confirm_to_quit)
#     button2.pack(side='right')
#     panel.pack(side='bottom')
#     #开启主事件循环
#     tkinter.mainloop()
#
# if __name__ == '__main__':
#     main()


"""
了解pygame
"""
# import pygame

# def main():
#     #初始化导入的pygame模块
#     pygame.init()
#     #初始化显示窗口参数
#     screen = pygame.display.set_mode((300, 533))
#     #设置当前窗口的标题
#     pygame.display.set_caption('大球吃小球')
#     #设置窗口的背景色
#     screen.fill((242, 242 ,242))
#     # 通过指定文件名加载图像
#     image = pygame.image.load(r'D:\ImageLib\joker_girl.jpg')
#     screen.blit(image, (0, 0))
#     #绘制一个圆（参数：屏幕，颜色，圆心位置，半径，0表示填充圆）
#     # pygame.draw.circle(screen, (255, 0, 0), (100, 100), 30, 0)
#     #刷新当前窗口(渲染窗口将绘制的图像呈现出来)
#     pygame.display.flip()
#
#     x, y = 50, 50
#     running = True
#     #开启另一个时间循环处理发生的事件
#     while running:
#         #从消息队列中获取事件并对事件进行处理
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 running = False
#
#         # screen.fill((255, 255, 255))
#         image = pygame.image.load(r'D:\ImageLib\joker_girl.jpg')
#         screen.blit(image, (0, 0))
#         pygame.draw.circle(screen, (255, 0, 0), (x, y), 30, 0)
#         pygame.display.flip()
#         pygame.time.delay(50)
#         x, y= x+5, y+5
#
#
# if __name__ == '__main__':
#     main()


#学习枚举：
from enum import Enum, unique, auto
# #默认从1开始标记
# Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))
#显式指定模块名字
# Month = Enum('Month', 'JAN FEB', module=__name__)
# for name, member in Month.__members__.items():
#     print(name, '=>', member, ',', member.value)
#
# class Color(Enum):
#     RED = 1
#     GREEN = 2
#     BLUE = 3
# print(Color.RED)
## print(repr(Color.RED))  # 输出更多的信息
# # print(type(Color.RED))
# # print(isinstance(Color.RED, Color))
# # print(Color.RED.name)
# # print(Color.RED.value)
#
# class Shake(Enum):
#     VANILLA = 7
#     CHOCOLATE = 4
#     COOKIES = 9
#     MINT = 3
#
# # for shake in Shake:
# #     print(shake)
#
# apples = {}
# apples[Color.RED] = 'red delicious'
# apples[Color.GREEN] = 'granny smith'
# for apple in apples.items():
#     print(apple)
# print(Color(1))

#值和标识都是唯一的
# @unique
# class Miatake(Enum):
#     ONE = 1
#     TWO = 2
#     THREE = 3
#     FOUR = 4
#
# class Color(Enum):
#     RED = auto()
#     BLUE = auto()
# for color in Color:
#     print(repr(color))

# class Autoname(Enum):
#     def _generate_next_value_(name, start, count, last_values):
#         return name
# class Ordinal(Autoname):
#     NORTH = auto()
#     SOUTH = auto()
#     EAST = auto()
#
# for i in Ordinal:
#     print(repr(i))
# Animal = Enum('Animal', 'ANT BEE CAT DOG')
# print(Animal)
# print(Animal.__members__)
# print(Animal.__members__.items())
# for a in Animal.__members__.items():
#     print(a, end=' ')
#     print(type(a), end=' ')
#     print(a[0], type(a[1]), a[1], a[1].value, end=' ')
# print(Animal['ANT'])
# print(Animal['ANT'].value)

# class Planet(Enum):
#     EARTH = (5.976e+24, 6.37814e+6)
#
#     def __init__(self, mass, radius):
#         self._mass = mass
#         self._radius = radius
#
#     @property
#     def surface_gravity(self):
#         G = 6.67300e-11
#         return G*self._mass / (self._radius*self._radius)
#
# print(Planet.EARTH.surface_gravity)
# print(dir(Planet))

#碰撞检测
from enum import Enum, unique
from math import sqrt
from random import randint

import pygame

@unique
class Color(Enum):
    RED = (255,0,0)
    GREEN = (0,255,0)
    BLUE = (0,0,255)
    BLACK = (0,0,0)
    WHITE = (255,255,255)
    GRAY = (242,242,242)

    @staticmethod
    def random_color():
        r = randint(0,255)
        g = randint(0,255)
        b = randint(0,255)

        return r,g,b

class Ball(object):
    def __init__(self, x, y, radius, sx, sy, color=Color.RED):
        self.x = x
        self.y = y
        self.radius = radius
        self.sx = sx
        self.sy = sy
        self.color = color
        self.alive = True

    def move(self, screen):
        #加一个判断初始位置的


        #检测左右屏幕间距是否超出
        if self.x - self.radius <= 0 \
                or self.x + self.radius >= screen.get_width():
            self.sx = -self.sx
        #上下边距
        if self.y - self.radius <= 0 \
                or self.y + self.radius >= screen.get_height():
            self.sy = -self.sy


        self.x += self.sx
        self.y += self.sy



    def eat(self, other):
        """吃掉其他球"""
        if self.alive and other.alive and self != other:
            dx, dy = self.x - other.x, self.y - other.y
            distance = sqrt(dx**2 + dy**2)
            if distance < self.radius + other.radius and self.radius > other.radius:
                other.alive = False
                self.radius = self.radius + int(other.radius * 0.146)

    def draw(self, screen):
        pygame.draw.circle(screen, self.color,(self.x, self.y), self.radius, 0)

#事件处理
def main():
    balls = []
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption('大球吃小球')
    running = True
    while running:
        #从消息队列中获取事件并进行处理
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            #处理鼠标事件的代码
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                #获取鼠标点击的位置
                x, y = event.pos
                radius = randint(10, 100)
                sx, sy = randint(-10, 10), randint(-10, 10)
                color = Color.random_color()
                ball = Ball(x, y, radius, sx, sy, color)
                balls.append(ball)

        screen.fill((255, 255, 255))
        #取出容器中的球，如果没被吃掉就绘制
        for ball in balls:
            if ball.alive:
                ball.draw(screen)
            else:
                balls.remove(ball)
        pygame.display.flip()
        pygame.time.delay(50)
        for ball in balls:
            ball.move(screen)
            for other in balls:
                ball.eat(other)

if __name__ == '__main__':
    main()