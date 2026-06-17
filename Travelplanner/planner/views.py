from django.shortcuts import render

def planner(request):
    return render(request, 'planner/home.html')
def about(request):
    return render(request, 'planner/about.html')
def popular_destinations(request):
    return render(request, 'planner/p_destinations.html')
def newsletter(request):
    return render(request, 'planner/newsletter.html')




