from django.conf import settings
from django.views import View
from django.http import HttpResponse
from django.shortcuts import render


def style_view(request):
    template_name = 'branding/branding.css'

    context = {}

    context['background_color'] = settings.BRANDING['COLORS']['Header']
    context['foreground_color'] = settings.BRANDING['COLORS']['HeaderForeground']

    return render(request, template_name, context, content_type='text/css')
