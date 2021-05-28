from practice.models import Practice
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.db.models import Q  # used to generate search request

# Create your views here.


class PracticeListView(ListView):
    model = Practice
    paginate_by = 10

    # see example at the following URL
    # https://learndjango.com/tutorials/django-search-tutorial

    def get_queryset(self):
        """[summary]
        Over ridded function in order to get results whatever the query is. 

        Returns:
            Practice: returning a list of practice according the query content 
        """
        query = self.request.GET.get('q')
        if query is not None:
            object_list = Practice.objects.filter(
                Q(label__icontains=query) | Q(description__icontains=query)
            )
        else:
            object_list = Practice.objects.all()  # In this case the query is empty
        return object_list

class PracticeDetailView(DetailView):

    model = Practice


