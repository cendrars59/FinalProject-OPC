from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin


@login_required
def information(request):
    # function the club information page
    # all the information into are static
    return render(request, "pages/information.html")


@login_required
def legal(request):
    # function the legal information page
    # all the information into are static
    return render(request, "pages/legal.html")


@login_required
def home(request):
    # Temp home page
    return render(request, "pages/home.html")
