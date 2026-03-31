from django.shortcuts import render

def planner(request):
    return render(request, 'planner/home.html')
def about(request):
    return render(request, 'planner/about.html')
def bookings(request):
    return render(request, 'planner/bookings.html')



