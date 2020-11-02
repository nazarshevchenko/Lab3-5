from django.shortcuts import render
from .models import Plane


# Create your views here.
def index(requests):
    create = Plane.objects.all()
    return render(requests, "hero/index.html", {'create': create})


def sort(requests):
    create = Plane.objects.order_by('price')
    return render(requests, "hero/index.html", {'create': create})


