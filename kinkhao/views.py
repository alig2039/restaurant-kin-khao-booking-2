from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, "index.html")


def menu(request):
    return render(request, "menu.html")


def reservations(request):
    return render(request, "reservations.html")