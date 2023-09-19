from django.shortcuts import render

# Create your views here.
def index(request):
    print('do smth')
    return render(request, 'main/index.html')
