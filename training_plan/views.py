from django.shortcuts import get_object_or_404
from training_plan.models import TrainingPlan
from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.db.models import Q  # used to generate search request
from training_plan.forms import AddForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
import os
from django.conf import settings
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
from django.contrib.staticfiles import finders


# Create your views here.


class TrainingPlanListView(LoginRequiredMixin, ListView):
    model = TrainingPlan
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
            object_list = TrainingPlan.objects.filter(
                Q(label__icontains=query) | Q(description__icontains=query)
            )
        else:
            object_list = TrainingPlan.objects.all()  # In this case the query is empty
        return object_list

class TrainingPlanDetailView(LoginRequiredMixin, DetailView):

    model = TrainingPlan

class TrainingPlanCreateView(LoginRequiredMixin, CreateView):

    model = TrainingPlan
    form_class = AddForm
    success_url = '/training_plans/'

class TrainingPlanUpdateView(LoginRequiredMixin, UpdateView):

    model = TrainingPlan
    form_class = AddForm
    success_url = '/training_plans/'

@login_required
def training_plan_pdf_view(request, *args, **kwargs):
    # View generating the pdf proving detailed information about the traing session 
    # View is built upon the following sources 
    # https://www.youtube.com/watch?v=J3MuH6xaDjI&list=WL&index=1
    # https://xhtml2pdf.readthedocs.io/en/latest/usage.html#using-xhtml2pdf-in-django
    pk = kwargs.get('pk')
    training_plan = get_object_or_404(TrainingPlan, pk=pk)
    template_path = 'training_plan/trainingplan-pdf.html'
    context = {'training_plan': training_plan}
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'filename="training-plan.pdf"'
    # find the template and render it.
    template = get_template(template_path)
    html = template.render(context)

    # create a pdf
    pisa_status = pisa.CreatePDF(
       html, dest=response)
    # if error then show some funy view
    if pisa_status.err:
       return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response
