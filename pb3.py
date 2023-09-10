import turtle

input_str = input("Enter a text of string : ")

def char_count( char : chr, text: str) :

    count = 0

    for i in text :
        if i == char :
            count += 1
    
    return count

def get_no_repeat(input_str) :
    res = ''
    for i in input_str :
        if i not in res :
            res = res + i
    return res


origin = (-200, 0)

vertical_tl = turtle.Turtle()
vertical_tl.penup()
vertical_tl.goto(origin[0], origin[1])
vertical_tl.pendown()
vertical_tl.left(90)
vertical_tl.forward(100)


turtle.penup()
gap_x = 20
bar_width = 15
turtle.goto(origin[0], origin[1])

for char in get_no_repeat(input_str) :

    frequency = char_count(char, input_str) 
    frequency = round(frequency, 3)

    turtle.pendown()
    turtle.forward(gap_x)

    turtle.penup()
    turtle.goto(turtle.xcor(), turtle.ycor() - 20)
    turtle.pendown()
    turtle.write(char)
    turtle.penup()
    turtle.goto(turtle.xcor(), turtle.ycor()+20)
    turtle.pendown()

    turtle.left(90)
    turtle.forward(frequency * 20)
    turtle.right(90)
    turtle.forward(bar_width)
    turtle.right(90)
    turtle.forward(frequency * 20)
    turtle.right(90)
    turtle.forward(bar_width)
    turtle.right(180)
    turtle.forward(bar_width + gap_x)
    


turtle.done()