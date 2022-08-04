#!/usr/bin/env python3 

from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.pdfgen import canvas

from reportlab.platypus import Table, TableStyle

def draw_calendar_circle():
    doc = canvas.Canvas("calendar_circle.pdf")

    radio = 10
    # create a function to generate an x and y to put on the paper

    # linear
    
    escala = 20
    linear_function = {}
    for n in range(1,10):
        n = n * escala
        x = n
        y = 3*x
        linear_function[x] = y
    
    dicc = linear_function
    print(dicc)
    
    for x, y in dicc.items():
        doc.circle(x, y, radio)

    doc.save()

if __name__ == '__main__':
    draw_calendar_circle()

