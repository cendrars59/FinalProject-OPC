from practice.models import Practice
from club.models import Season
from users.models import CustomUser, Role, InvolvedAsICategoryForSeason
from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.db.models import Q  # used to generate search request
from practice.forms import AddForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.


class PracticeListView(LoginRequiredMixin, ListView):
    model = Practice
    paginate_by = 10

    # see example at the following URL
    # https://learndjango.com/tutorials/django-search-tutorial

    def get_queryset(self):
        """[summary]
        Over ridded function in order to get results whatever the query is. 

        Returns:
            Practice: returning a list of practice according the query content 
            or all practices if no query 
        """
        query = self.request.GET.get('q')
        if query is not None:

            object_list = Practice.objects.filter(
                Q(label__icontains=query) | Q(description__icontains=query)
            )

        else:
            object_list = Practice.objects.all()  # In this case the query is empty
        return object_list

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)
        context["active_season"] = Season.get_active_season()
        return context


class PracticeDetailView(LoginRequiredMixin, DetailView):

    model = Practice

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)
        context["active_season"] = Season.get_active_season()
        return context


class PracticeCreateView(LoginRequiredMixin, CreateView):

    model = Practice
    form_class = AddForm
    success_url = '/practices/'

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)
        context["active_season"] = Season.get_active_season()
        return context


class PracticeUpdateView(LoginRequiredMixin, UpdateView):

    model = Practice
    form_class = AddForm
    success_url = '/practices/'

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)
        context["active_season"] = Season.get_active_season()
        return context
