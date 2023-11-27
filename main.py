"""
Case-Study №5
Developers: Kuznetsov N. 100%
            Shishko S. 100%

"""

import turtle

#1:
def recurse(n, size):
    turtle.colormode(255)
    cg = 255 - int(n * 8) % 255
    turtle.color(int((255-2*cg)*(1-(cg//128))), int(2*cg - 4*(cg-128)*(cg//128)), int((cg//128)*(cg-128)*2))
    if n == 0: return
    for _ in range(4):
        turtle.forward(size)
        turtle.right(90)
    turtle.forward(size / 10)
    turtle.right(10)
    recurse(n - 1,  size * 0.9)

#2:
def color_tree(depth, size):
  turtle.colormode(255)
  cg = 255 - int(depth * (250 / 6)) % 255
  turtle.color(0, cg, 0)
  if depth == 0:
    turtle.forward(size)
    turtle.backward(size)
  else:
    turtle.forward(size)
    turtle.right(30)
    color_tree(depth - 1, size / 2)

    turtle.left(60)
    color_tree(depth - 1, size / 2)
    turtle.right(30)
    cg = 255 - int(depth * (250 / 6)) % 255
    turtle.color(0, cg, 0)
    turtle.backward(size)

#3:
def branch(n, size):
    if n == 0:
        turtle.left(180)
        return

    x = size/(n+1)
    for i in range(n):
        turtle.forward(x)
        turtle.left(45)
        branch(n-i-1, 0.5*x*(n-i-1))
        turtle.left(90)
        branch(n-i-1, 0.5*x*(n-i-1))
        turtle.right(135)

    turtle.forward(x)
    turtle.left(180)
    turtle.forward(size)

#4:
def koch(order, size):
    if order == 0:
        turtle.forward(size)
    else:
        koch(order-1, size/3)
        turtle.left(60)
        koch(order-1, size/3)
        turtle.right(120)
        koch(order-1, size/3)
        turtle.left(60)
        koch(order-1, size/3)

#5:
def koch_snowflake(order, size):
    for _ in range(3):
        koch(order, size)
        turtle.right(120)

#6:
def mincov(n, a):
  if n == 0:
      turtle.forward(a)
  else:
      mincov(n-1, a/4)
      turtle.left(90)
      mincov(n-1, a/4)
      turtle.right(90)
      mincov(n-1, a/4)
      turtle.right(90)
      mincov(n-1, a/2)
      turtle.left(90)
      mincov(n-1, a/4)
      turtle.left(90)
      mincov(n-1, a/4)
      turtle.right(90)
      mincov(n-1, a/4)

#7:
def ice(n, a):
   if n == 0:
       turtle.forward(a)
   else:
       ice(n-1, a/1.25)
       turtle.left(90)
       ice(n-1, a/2.5)
       turtle.right(180)
       ice(n-1, a/2.5)
       turtle.left(90)
       ice(n-1, a/1.25)

#8:
def ice_2(n, a):
   if n == 0:
       turtle.forward(a)
   else:
       ice_2(n-1, a/1.25)
       turtle.left(120)
       ice_2(n-1, a/2.5)
       turtle.right(180)
       ice_2(n-1, a/2.5)
       turtle.left(120)
       ice_2(n-1, a/2.5)
       turtle.left(180)
       ice_2(n-1, a/2.5)
       turtle.left(120)
       ice_2(n-1, a/1.25)

#9:
def levy(n, a):
   if n == 0:
       turtle.forward(a)
   else:
       turtle.left(45)
       levy(n-1, a/1.25)
       turtle.right(90)
       levy(n-1, a/1.25)
       turtle.left(45)

#10:
def some_fractal(n, size):
    if n == 0:
        turtle.fillcolor('black')
        turtle.begin_fill()
        for _ in range(3):
            turtle.forward(size)
            turtle.left(120)
        turtle.end_fill()

    else:
        some_fractal(n-1, size/2)
        turtle.left(60)
        turtle.forward(size/2)
        turtle.right(60)
        some_fractal(n-1, size/2)
        turtle.right(60)
        turtle.forward(size/2)
        turtle.left(60)
        some_fractal(n-1, size/2)
        turtle.back(size/2)

#11:
def dragon(n, size, k = 1):

    if n == 0:
        turtle.forward(size)
    else:
        turtle.left(45)
        dragon(n-1, size, 1)
        turtle.right(k*90)
        dragon(n-1, size, -1)
        turtle.right(45)

#drawing function:
def draw_fractal(name, depth, size):
    if name == 1: recurse(depth, size)
    elif name == 2:
        turtle.left(90)
        color_tree(depth, size)
    elif name == 3:
        turtle.left(90)
        branch(depth, size)
    elif name == 4: koch(depth, size)
    elif name == 5: koch_snowflake(depth, size)
    elif name == 6: mincov(depth, size)
    elif name == 7: ice(depth, size)
    elif name == 8: ice_2(depth, size)
    elif name == 9: levy(depth, size)
    elif name == 10: some_fractal(depth, size)
    elif name == 11: dragon(depth, size)

print('1: Квадратная рекурсия',
      '2: Двоичное дерево',
      '3: Фрактал "Ветка"',
      '4: Кривая Коха',
      '5: Снежинка Коха',
      '6: Кривая Минковского',
      '7: Ледяной фрактал 1',
      '8: Ледяной фрактал 2',
      '9: Кривая Леви',
      '10: Треугольник Серпинского',
      '11: Фрактал Дракон Хартера-Хейтуэя',
      'Выберите номер фрактала:',sep='\n'
      )

number = int(input())

depth = int(input('Введите глубину фрактала: '))
size = int(input('Введите размер фрактала: '))


turtle.speed(0)
draw_fractal(number, depth, size)

turtle.done()