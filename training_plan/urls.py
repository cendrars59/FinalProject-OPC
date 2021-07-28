"""config URL Configuration.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static  # Used only for dev purpose.
from django.conf import settings  # Used only for dev purpose.
from training_plan.views import (TrainingPlanListView,
TrainingPlanDetailView, TrainingPlanCreateView, TrainingPlanUpdateView,
training_plan_pdf_view)

urlpatterns = [
    path('', TrainingPlanListView.as_view(), name='training_plan-list'),
    path('new/', TrainingPlanCreateView.as_view(), name='training_plan-new'),
    path('<pk>/', TrainingPlanDetailView.as_view(), name='training_plan-detail'),
    path('<pk>/update', TrainingPlanUpdateView.as_view(), name='training_plan-update'),
    path('training_plan_pdf/<pk>',training_plan_pdf_view, name='training_plan_pdf'),
]

# In context of dev (Debug is set) the following configuration will be applied
# Because using the django application we need to emulate a real server sttings
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)