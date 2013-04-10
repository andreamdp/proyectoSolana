#encoding= utf-8
# Create your views here.
from django.views.generic.simple import direct_to_template 
from django.http import HttpResponse
from django.views.generic import ListView
from django.forms.models import inlineformset_factory
from reportlab.lib.colors import navy, yellow, red, black, blue
from django.http import HttpResponse
from geraldo import Report, DetailBand, ObjectValue
from geraldo.generators import PDFGenerator
from geraldo.utils import cm

from clientes.models import ConjuntoObra, Cliente, Obra, Cobro, Costo

from geraldo import Report, DetailBand, ObjectValue
from geraldo.utils import cm
from geraldo.generators import PDFGenerator
from django.core.exceptions import PermissionDenied
from reportlab.lib.pagesizes import legal
from geraldo import Report, ReportBand, Label, ObjectValue, SystemField,\
    FIELD_ACTION_COUNT, FIELD_ACTION_AVG, FIELD_ACTION_MIN,\
    FIELD_ACTION_MAX, FIELD_ACTION_SUM, FIELD_ACTION_DISTINCT_COUNT, BAND_WIDTH,\
    RoundRect, Line, landscape
from reportlab.lib.enums import TA_CENTER, TA_JUSTIFY, TA_RIGHT


class ReporteClientes(Report):
    title = 'Listado de Clientes'
    page_size = landscape(legal)
    class band_page_header(ReportBand):
        height = 2.7*cm
        elements = [
            SystemField(expression='%(report_title)s', top=0.1*cm, left=0, width=BAND_WIDTH,
                style={'fontName': 'Helvetica-Bold', 'fontSize': 20, 'alignment': TA_CENTER,  'textColor': navy}),
            Label(text="Nombre", top=2*cm, left=0),
            Label(text="Apellido", top=2*cm, left=3.5*cm),
            Label(text="Razón Social", top=2*cm, left=7.6*cm),
            Label(text="Nro. de Cliente", top=2*cm, left=12*cm),
            Label(text="Direccion", top=2*cm, left=16.2*cm),
            Label(text="Altura", top=2*cm, left=19*cm),
            Label(text="Ciudad", top=2*cm, left=21.5*cm),
            Label(text="Provincia", top=2*cm, left=26*cm),
            Label(text="Pais", top=2*cm, left=29.4*cm),
        ]
        borders = {'bottom': Line(stroke_color=black, stroke_width=1)}
    class band_detail(DetailBand):
        height=0.7*cm
        elements=[
        ObjectValue(attribute_name='nombre', top=0.1*cm, left=0),
            ObjectValue(attribute_name='apellido', top=0.1*cm, left=3.6*cm),
            ObjectValue(attribute_name='razon_social', top=0.1*cm, left=7.6*cm),
            ObjectValue(attribute_name='cliente_nro', top=0.1*cm, left=12*cm),
            ObjectValue(attribute_name='direccion', top=0.1*cm, left=16.2*cm),
            ObjectValue(attribute_name='altura', top=0.1*cm, left=19*cm),
            ObjectValue(attribute_name='ciudad', top=0.1*cm, left=21.5*cm),
            ObjectValue(attribute_name='provincia', top=0.1*cm, left=26*cm),
            ObjectValue(attribute_name='pais', top=0.1*cm, left=29.5*cm),
           
            
            
            ]

def v_ListadoClientes(request):
    response = HttpResponse(mimetype='application/pdf')
    objects_list = Cliente.objects.all() # If you are using Django
    report = ReporteClientes(queryset=objects_list)
    report.generate_by(PDFGenerator, filename=response)

    return response

    
class ReporteObras(Report):
    title = 'Listado de Obras'
    page_size = landscape(legal)
    class band_page_header(ReportBand):
        height = 2.7*cm
        elements = [
            SystemField(expression='%(report_title)s', top=0.1*cm, left=0, width=BAND_WIDTH,
                style={'fontName': 'Helvetica-Bold', 'fontSize': 20, 'alignment': TA_CENTER,  'textColor': navy}),
            Label(text="Nombre", top=2*cm, left=0),
            Label(text="Cliente", top=2*cm, left=10*cm),
            Label(text="Ciudad", top=2*cm, left=16*cm),
            Label(text="Estado", top=2*cm, left=22*cm),
            Label(text="Director de Obra", top=2*cm, left=25*cm),
            
        ]
        borders = {'bottom': Line(stroke_color=black, stroke_width=1)}
    class band_detail(DetailBand):
        height=0.7*cm
        elements=[
        ObjectValue(attribute_name='nombre', top=0.1*cm, left=0),
            ObjectValue(attribute_name='cliente', top=0.1*cm, left=10*cm),
            ObjectValue(attribute_name='ciudad', top=0.1*cm, left=16*cm),
            ObjectValue(attribute_name='estado', top=0.1*cm, left=22*cm),
            ObjectValue(attribute_name='director_obra', top=0.1*cm, left=25*cm),
            
           
            
            
            ]

def v_ListadoObras(request):
    response = HttpResponse(mimetype='application/pdf')
    objects_list = ConjuntoObra.objects.all() # If you are using Django
    report = ReporteObras(queryset=objects_list)
    report.generate_by(PDFGenerator, filename=response)

    return response


class ReporteCobros(Report):
    title = 'Listado de Cobros'
    page_size = landscape(legal)
    class band_page_header(ReportBand):
        height = 2.7*cm
        elements = [
            SystemField(expression='%(report_title)s', top=0.1*cm, left=0, width=BAND_WIDTH,
                style={'fontName': 'Helvetica-Bold', 'fontSize': 20, 'alignment': TA_CENTER,  'textColor': navy}),
            Label(text="Obra", top=2*cm, left=0),
            Label(text="Tipo de Cobro", top=2*cm, left=10*cm),
            Label(text="Fecha", top=2*cm, left=16*cm),
            Label(text="Importe", top=2*cm, left=22*cm),
            Label(text="observaciones", top=2*cm, left=25*cm),
            
        ]
        borders = {'bottom': Line(stroke_color=black, stroke_width=1)}
    class band_detail(DetailBand):
        height=0.7*cm
        elements=[
        ObjectValue(attribute_name='conjunto_obra', top=0.1*cm, left=0),
            ObjectValue(attribute_name='tipo_cobro', top=0.1*cm, left=10*cm),
            ObjectValue(attribute_name='fecha', top=0.1*cm, left=16*cm),
            ObjectValue(attribute_name='importe', top=0.1*cm, left=22*cm),
            ObjectValue(attribute_name='observaciones', top=0.1*cm, left=25*cm),
            
           
            
            
            ]

def v_ListadoCobros(request):
    response = HttpResponse(mimetype='application/pdf')
    objects_list = Cobro.objects.all() # If you are using Django
    report = ReporteCobros(queryset=objects_list)
    report.generate_by(PDFGenerator, filename=response)

    return response

class ReporteCostos(Report):
    title = 'Listado de Costos'
    page_size = landscape(legal)
    class band_page_header(ReportBand):
        height = 2.7*cm
        elements = [
            SystemField(expression='%(report_title)s', top=0.1*cm, left=0, width=BAND_WIDTH,
                style={'fontName': 'Helvetica-Bold', 'fontSize': 20, 'alignment': TA_CENTER,  'textColor': navy}),
            Label(text="Costo", top=2*cm, left=0),
            Label(text="Tipo de Recurso", top=2*cm, left=10*cm),
            Label(text="Recurso", top=2*cm, left=16*cm),
            Label(text="Cantidad", top=2*cm, left=22*cm),
            Label(text="Total", top=2*cm, left=25*cm),
            
        ]
        borders = {'bottom': Line(stroke_color=black, stroke_width=1)}
    class band_detail(DetailBand):
        height=0.7*cm
        elements=[
        ObjectValue(attribute_name='conjunto_costo', top=0.1*cm, left=0),
            ObjectValue(attribute_name='tipo', top=0.1*cm, left=10*cm),
            ObjectValue(attribute_name='recurso', top=0.1*cm, left=16*cm),
            ObjectValue(attribute_name='cantidad', top=0.1*cm, left=22*cm),
            ObjectValue(attribute_name='total', top=0.1*cm, left=25*cm),
            
           
            
            
            ]

def v_ListadoCostos(request):
    response = HttpResponse(mimetype='application/pdf')
    objects_list = Costo.objects.all() # If you are using Django
    report = ReporteCostos(queryset=objects_list)
    report.generate_by(PDFGenerator, filename=response)

    return response

from geraldo import Report, landscape, ReportBand, ObjectValue, SystemField,\
        BAND_WIDTH, Label, ReportGroup, SubReport
subreports = [
        SubReport(
            queryset_string = '%(object)s.obra_set.all()',
            detail_band = ReportBand(
                height=0.5*cm,
                elements=[
                    ObjectValue(attribute_name='tipo_obra', top=0, left=1*cm),
                    ObjectValue(attribute_name='observacion', top=0, left=5*cm),
                    ]
                ),
            ),
        ]
