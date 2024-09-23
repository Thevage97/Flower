import turtle
import colorsys as cs

def draw_pattern():
    turtle.setup(800, 2003)
    turtle.speed(0)
    turtle.width(2)
    turtle.bgcolor("black")
    
    for i in range(25):
        for j in range(15):
            turtle.color(cs.hsv_to_rgb(i/15, 5/25, 1))
            turtle.right(90)
            turtle.circle(200-j*4, 90)
            turtle.left(90)
            turtle.circle(200-j*4, 90)
            turtle.right(180)
            turtle.circle(50, 24)
    
    turtle.hideturtle()
    turtle.done()

# Call the function to draw the pattern
draw_pattern()
