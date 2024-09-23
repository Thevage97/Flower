import turtle
import colorsys as cs

def draw_turtle_art():
    turtle.tracer(100)
    h = 0.85
    turtle.speed(25)
    turtle.bgcolor("black")
    
    for i in range(190):
        c = colorsys.hsv_to_rgb(h,1,1)
        turtle.fillcolor(c)
        h += 0.0015
        turtle.begin_fill()
        turtle.circle(190-i, 90)
        turtle.lt(75)
        turtle.lt(20)
        turtle.circle(190-i, 90)
        turtle.lt(18)
        turtle.end_fill()
    
    turtle.done()

if __name__ == "__main__":
    draw_turtle_art()
