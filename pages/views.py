from django.shortcuts import render


def information(request):
    # function the club information page
    # all the information into are static
    return render(request, "pages/information.html")


def legal(request):
    # function the legal information page
    # all the information into are static
    return render(request, "pages/legal.html")


def home(request):
    # function the club information page
    # all the information into are static
    return render(request, "pages/home.html")
