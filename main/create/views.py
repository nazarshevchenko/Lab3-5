from django.shortcuts import render

# Create your views here.
def index(requests):
    create = Plane.objects.all()
    return render(requests, "create/index.html")
