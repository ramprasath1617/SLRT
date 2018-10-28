from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'tool/home.html', {})

def app(request):
    return render(request, 'tool/app.html', {})