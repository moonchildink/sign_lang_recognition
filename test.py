以下是一个简单的 Python Turtle 绘制相机的示例代码：

python
Copy code
import turtle

# 创建一个窗口和画布
window = turtle.Screen()
canvas = window.getcanvas()

# 设置画笔颜色和尺寸
turtle.pensize(3)
turtle.pencolor("black")

# 绘制相机主体
turtle.fillcolor("black")
turtle.begin_fill()
turtle.left(90)
turtle.forward(100)
turtle.right(90)
turtle.forward(50)
turtle.right(90)
turtle.forward(100)
turtle.right(90)
turtle.forward(50)
turtle.end_fill()

# 绘制相机镜头
turtle.penup()
turtle.goto(25, 60)
turtle.pendown()
turtle.fillcolor("gray")
turtle.begin_fill()
turtle.circle(10)
turtle.end_fill()

# 绘制相机闪光灯
turtle.penup()
turtle.goto(-25, 60)
turtle.pendown()
turtle.fillcolor("gray")
turtle.begin_fill()
turtle.circle(10)
turtle.end_fill()

# 隐藏画笔
turtle.hideturtle()

# 显示窗口
window.mainloop()