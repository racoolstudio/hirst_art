from turtle import *
import  random
my_turtle = Turtle()
my_turtle.shape('turtle')
my_turtle.color('green')
t = my_turtle
#
colormode(255)
# # for i in range(4):
# #     t.fd(200)
# #     t.right(90)
# # for i in range (10):
# #     t.pendown()
# #     t.fd(10)
# #     t.penup()
# #     t.fd(10)
#
#
# # for i in range(3,8):
# #     for j in range(i):
# #         t.color(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
# #         t.fd(100)
# #         t.rt(360/i)
# num = random.randint(0, 255)
#
# # for i in range(3):
# #
# #     j = random.randint(0, 255)
# # #     directions = [t.left(j), t.right(j), ]
# #     t.forward(100)
# #     random.choice(directions)
# #     t.forward(100)
#
# # directions = [0, 90, 180, 270]
# # t.speed(60)
# # for i in range(500):
# #  t.seth(random.choice(directions))
# #  t.forward(30)
# # for j in range(5):
# #
# #     t.penup()
# #     t.forward(30)
# #     t.pendown()
# #     t.circle(10)
# t.speed('fastest')
# def spirogyra(size):
#     for i in range(360//size):
#         t.color(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
#         pendown()
#         t.circle(100)
#         penup()
#         t.seth(t.heading() + size)
# spirogyra(5)
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#

# import colorgram
# color = colorgram.extract('image.jpg',10)
# print(color[0].rgb[0])
# list =[]
# for i in range(10):
#     list.append((color[i].rgb[0], color[i].rgb[1], color[i].rgb[2]))
#

color_list =[(245, 243, 238), (246, 242, 244), (202, 164, 110), (240, 245, 241), (236, 239, 243), (149, 75, 50), (222, 201, 136), (53, 93, 123), (170, 154, 41), (138, 31, 20)]

def draw_row():
    for i in range(10):
        t.pendown()
        t.color(random.choice(color_list))
        t.dot(20)
        t.penup()
        t.forward(50)
# for i in range(10):
#
#     draw_row()
#     t.penup()
#     t.seth(t.heading()+90)
#     t.forward(50)
for i in range(10):
    draw_row()
    print('\n')


myScreen = Screen()

myScreen.exitonclick()

