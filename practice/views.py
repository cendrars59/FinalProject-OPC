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

    # managing get & queryset function
    # http://www.intelligent-d2.com/python/django/use-get-get_queryset-get_context_data-django/#:~:text=The%20get_queryset%20method%20is%20used%20whenever%20data%20is,view%20will%20retrieve%20all%20data%20from%20the%20database.

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


class PracticeDetailView(LoginRequiredMixin, DetailView):

    model = Practice


class PracticeCreateView(LoginRequiredMixin, CreateView):

    model = Practice
    form_class = AddForm
    success_url = '/practices/'


class PracticeUpdateView(LoginRequiredMixin, UpdateView):

    model = Practice
    form_class = AddForm
    success_url = '/practices/'
