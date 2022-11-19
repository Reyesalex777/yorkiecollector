from django.shortcuts import render

yorkies = [
    {'name': 'Lolo', 'breed': 'yorkies', 'description': 'stuck up and spoiled', 'age': 3},
    {'name': 'Sachi', 'breed': 'teacup yorkie', 'description': 'gentle and loving', 'age': 2},
]

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def yorkies_index(request):
    return render(request, 'yorkies/index.html', { 'yorkies': yorkies })