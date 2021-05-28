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
from practice import views
from django.conf.urls.static import static  # Used only for dev purpose.
from django.conf import settings  # Used only for dev purpose.
from practice.views import PracticeListView, PracticeDetailView

urlpatterns = [
    path('', PracticeListView.as_view(), name='practices-list'),
    path('<pk>/', PracticeDetailView.as_view(), name='practice-detail'),
]

# In context of dev (Debug is set) the following configuration will be applied
# Because using the django application we need to emulate a real server sttings
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
