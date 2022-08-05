#!/usr/bin/env python3 

from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

def draw_calendar_circle():
    doc = canvas.Canvas("calendar_circle.pdf")

    # create a function to generate an x and y to put on the paper

    # linear funtion
    escala = 20
    linear_function = {}
    for n in range(1,10):
        n = n * escala
        x = n
        y = 3*x
        linear_function[x] = y

    # draw
    radio = 4
    escala = 11
    linear = []
    for m in range(1, 8):
        for n in range(1, 54):
            n = n * escala
            x = n
            y = m * escala
            linear.append([x,y])
    
    array = linear
    print(array)
    
    for center in array:
        doc.circle(center[0],center[1], radio)

    # put days to calendar and months
    # put color to difference.
    # thinking in another way to draw circles is through grids.

    doc.save()

if __name__ == '__main__':
    draw_calendar_circle()

