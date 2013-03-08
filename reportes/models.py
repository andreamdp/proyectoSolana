from django.db import models

# Create your models here.
from solanaABM012.geraldo import Report, DetailBand, ObjectValue
from solanaABM012.geraldo.utils import cm
from solanaABM012.geraldo.generators import PDFGenerator

names = ['Mychelle', 'Leticia', 'Tarsila', 'Marta', 'Vera', 'Leni']

class MyReport(Report):
    class band_detail(DetailBand):
        height=0.7*cm
        elements=[
            ObjectValue(attribute_name='capitalize'),
            ]

report = MyReport(queryset=names)
report.generate_by(PDFGenerator, filename='female-names.pdf') 

import os
cur_dir = os.path.dirname(os.path.abspath(__file__))

from django.contrib.auth.models import User

from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm
from reportlab.lib.enums import TA_CENTER, TA_JUSTIFY, TA_RIGHT
from reportlab.lib.colors import navy, yellow, red, black, blue, lawngreen
from geraldo import Report, ReportBand, Label, ObjectValue, SystemField,\
    FIELD_ACTION_COUNT, FIELD_ACTION_AVG, FIELD_ACTION_MIN,\
    FIELD_ACTION_MAX, FIELD_ACTION_SUM, FIELD_ACTION_DISTINCT_COUNT, BAND_WIDTH,\
    RoundRect, Line, landscape

from geraldo.base import EmptyQueryset
from reportlab.lib.pagesizes import legal
from reportlab.lib.units import cm


class UsersReport(Report):
    title = 'Listado' 
   # page_size = landscape(legal)
    margin_left = 2*cm
    margin_top = 0.5*cm
    margin_right = 0.5*cm
    margin_bottom = 0.5*cm
    class band_page_header(ReportBand):
       # height = 1.3*cm
        elements = [
           # SystemField(expression='%(report_title)s', top=0.1*cm, left=0, width=BAND_WIDTH,
            #    style={'fontName': 'Helvetica-Bold', 'fontSize': 14, 'alignment': TA_CENTER}),
            Label(text="ID", top=0.8*cm, left=0),
            Label(text="name", top=0.8*cm, left=3*cm),
            Label(text="", top=0.8*cm, left=8*cm),
            Label(text="", top=0.8*cm, left=13*cm),
            Label(text="", top=0.8*cm, left=18*cm),
        ]
        borders = {'bottom': Line(stroke_color=navy)}

    class band_page_footer(ReportBand):
        #height = 0.4*cm
        elements = [
            Label(text='Sistema de Seguimiento de Obras', top=0.1*cm,
                right=0),
            SystemField(expression='%(now:%Y, %b %d)s', top=0.1*cm,
                width=BAND_WIDTH, style={'alignment': TA_RIGHT}),
        ]
        borders = {'top': Line(stroke_color=blue, stroke_width=1)}

    class band_detail(DetailBand):
        #height=0.7*cm
        elements=[
            ObjectValue(attribute_name='capitalize'),
            ]

