from django.shortcuts import render


def index(request):
    print('do smth')
    return render(request, 'main/index.html')
