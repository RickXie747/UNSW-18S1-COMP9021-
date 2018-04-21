from turtle import *

edge_length = 60
angle = 60


def draw_dodecagram(colour1,colour2):
    left(180 - angle)
    color('white')
    forward(edge_length)


    right(angle)
    for _ in range(3):
        color(colour1)
        forward(edge_length)
        right(180 - angle)
        forward(edge_length)
        color('white')
        forward(edge_length)

    left(180 - angle)
    for _ in range(3):
        color(colour2)
        forward(edge_length)
        left(180 - angle)
        forward(edge_length)
        color('white')
        forward(edge_length)


def teleport(distance):
    penup()
    forward(distance)
    pendown()


# Make sure that the dodecagrams are centred horizontally in the window that displays them.
# Without the following statement, the left end of the horizontal edge of the green dodecagram,
# from which the drawing starts, would be at the centre of the screen
# (so the dodecagrams are not quite centred vertically).

# Draw the middle dodecagram, then the left dodecagram, then the right dodecagram.
draw_dodecagram('red','blue')


