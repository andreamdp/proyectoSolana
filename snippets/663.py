# -*- coding:utf-8 -*-
#
# Use the tag like this:
#
# {% draw_form form fieldsets %}
#
# Where 'form' is the form to be draw and 'fieldsets' is a tuple containing the
# fieldsets and the contained fields.
#
# Example on how to build the fieldsets parameter
#
# fiedsets = (
#     ('Personal Data', {'fields':('name','gender'), 'id':'personal_data'}),
#     ('Address', {'fields':('street','number','city','zip_code'), 'id':'address'}),
# )
#

from django.template import Library

register = Library()

@register.simple_tag
def draw_form(form, fieldsets=False):
    i = 900
    return (i)
