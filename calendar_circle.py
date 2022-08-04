#!/usr/bin/env python3 

from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.pdfgen import canvas

from reportlab.platypus import Table, TableStyle

def draw_calendar_circle():
    # doc = canvas.Canvas("calendar_circle.pdf")
    # doc.setStrokeColorRGB(0.2, 0.5, 0.3)

    # data= [['00', '01', '02', '03', '04'],
    # ['10', '11', '12', '13', '14'],
    # ['20', '21', '22', '23', '24'],
    # ['30', '31', '32', '33', '34']]

    # t=Table(data)
    # t.setStyle(TableStyle([('BACKGROUND',(1,1),(-2,-2),colors.green),
    # ('TEXTCOLOR',(0,0),(1,-1),colors.red)]))
    # t.drawOn(doc, 0.75*inch, 0.5*inch)

    # doc.save()
    filename = 'pdf_test.pdf'
    p = canvas.Canvas(filename)
    p.circle(300, 600, 50)
    # table_data = [['O', 'O', 'O'], ['O', 'O', 'O']]
    table_data = [[p.circle(300,600,30),p.circle(300,600,10), 'O'], ['O', 'O', 'O']]
    top_row = Table(table_data)
    w, h = top_row.wrapOn(p, 0, 0)
    top_row.drawOn(p, 0.75*inch, 0.5*inch)
    p.showPage()
    p.save()
if __name__ == '__main__':
    draw_calendar_circle()

