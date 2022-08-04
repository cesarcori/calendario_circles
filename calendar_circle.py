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

    dicc = {10:20, 30:40, 50:60}
    
    for x, y in dicc.items():
        doc.circle(x, y, radio)

    doc.save()

if __name__ == '__main__':
    draw_calendar_circle()

