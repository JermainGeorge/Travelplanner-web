from django.shortcuts import render


def home(request):
    return render(request, 'homepg/index.html')

def about(request):
    return render(request, 'homepg/index2.html')