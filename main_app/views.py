from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Yorkie

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def yorkies_index(request):
    yorkies = Yorkie.objects.all()
    return render(request, 'yorkies/index.html', { 'yorkies': yorkies })

def yorkies_detail(request, yorkie_id):
    yorkie = Yorkie.objects.get(id=yorkie_id)
    return render(request, 'yorkies/detail.html', {
        'yorkie': yorkie
    })

class YorkieCreate(CreateView):
    model = Yorkie
    fields = '__all__'
    
class YorkieUpdate(UpdateView):
    model = Yorkie
    fields = ['breed', 'description', 'age']

class YorkieDelete(DeleteView):
    model = Yorkie
    success_url = '/yorkies'