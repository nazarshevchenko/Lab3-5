from django.shortcuts import render, redirect
from .models import Plane
from .forms import PlaneForm
from django.views.generic import DetailView, UpdateView, DeleteView
from .filters import SearchFilter
# Create your views here.

class Detail(DetailView):
    model = Plane
    template_name = 'hero/detail.html'
    context_object_name = 'plane'

class NewData(UpdateView):
    model = Plane
    template_name = 'hero/create.html'
    
    form_class = PlaneForm

class Delete(DeleteView):
    model = Plane
    success_url = '/'
    template_name = 'hero/delete.html'
    


def index(requests):
    sum = 0
    create = Plane.objects.all()

    if requests.method == "GET":
        if requests.GET.get('clear', '') != '':
            return redirect('/')

    if requests.method == "POST":

        if requests.POST.get('sort', 0):
            create = Plane.objects.order_by('price')
        if requests.POST.get('count', 0):
            for i in create:
                display_type = requests.POST.get(str(i.id), 0)
                if display_type:
                    sum += i.price
        
        if requests.POST.get('update', '') != '':
            return redirect(requests.POST.get('update', ''))

        if requests.POST.get('delete', '') != '':
            return redirect(requests.POST.get('delete', ''))
 
    
    
    myFilter = SearchFilter(requests.GET, queryset=create) 
    create = myFilter.qs       
    form = PlaneForm
    data = {
        'form': form,
        'count': sum,
        'create': create,
        'filter': myFilter
    }
    return render(requests, "hero/index.html", data)


def sort(requests):
    create = Plane.objects.order_by('price')
    return render(requests, "hero/index.html", {'create': create})

def create(requests):
    error = ''
    if requests.method == "POST":
        form = PlaneForm(requests.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            error = "Error. Please, try again"
    form = PlaneForm 

    data = {
        "form": form,
        "error": error
    }
    return render(requests, "hero/create.html", data)