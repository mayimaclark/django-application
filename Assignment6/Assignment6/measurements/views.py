from django.template import loader
from django.http import HttpResponse
from measurements.models import Area


def index(request):

    area_list = Area.objects.all()
    template = loader.get_template('measurements/measurements.html')
    context = {
        'area_list': area_list,
    }
    return HttpResponse(template.render(context, request))
