import turtle


def tree(branch_len):
    # 树干太短则不画,即为递归结束条件
    if branch_len > 5:
        # 画树干
        t.forward(branch_len)
        # 右倾斜20度
        t.right(20)
        # 递归调用，画右边的小树，树干减15
        tree(branch_len - 15)
        # 向左回40度，即左倾斜20度
        t.left(40)
        # 递归调用，画左边的小树，树干减15
        tree(branch_len - 15)
        # 向右回20度，即回正
        t.right(20)
        # 海龟退回原位置
        t.backward(branch_len)


t = turtle.Turtle()
t.left(90)
t.penup()
t.backward(100)
t.pendown()
t.pencolor('green')
t.pensize(2)
tree(75)
t.hideturtle()
turtle.done