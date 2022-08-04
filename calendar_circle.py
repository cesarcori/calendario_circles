#!/usr/bin/env python3 

from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

def draw_calendar_circle():
    c = canvas.Canvas("calendar_circle.pdf")
    c.setStrokeColorRGB(0.2, 0.5, 0.3)
    c.circle(300, 600, 50)
    c.save()

if __name__ == '__main__':
    draw_calendar_circle()

