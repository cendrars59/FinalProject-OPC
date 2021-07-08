from training_session.models import TrainingSession
from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.db.models import Q  # used to generate search request
from practice.forms import AddForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.


class TrainingSessionListView(LoginRequiredMixin, ListView):
    model = TrainingSession
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
            object_list = TrainingSession.objects.filter(
                Q(label__icontains=query) | Q(description__icontains=query)
            )
        else:
            object_list = TrainingSession.objects.all()  # In this case the query is empty
        return object_list

class TrainingSessionDetailView(LoginRequiredMixin, DetailView):

    model = TrainingSession

class TrainingSessionCreateView(LoginRequiredMixin, CreateView):

    model = TrainingSession
    form_class = AddForm
    success_url = '/training_sessions/'

class TrainingSessionUpdateView(LoginRequiredMixin, UpdateView):

    model = TrainingSession
    form_class = AddForm
    success_url = '/training_sessions/'