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
from django.contrib.auth import views as auth_views  # Used to mamage the authentification views provided by Django
from django.urls import path, include
from django.conf.urls.static import static  # Used only for dev purpose.
from django.conf import settings  # Used only for dev purpose.
from pages import views, urls
from practice import views, urls
from training_session import views, urls
from training_plan import views, urls
from users import views
from users.views import CustomUserUpdateView, PlayerListView, ManagerListView


urlpatterns = [
    path('admin/', admin.site.urls),
    # template name is used in order to not use the default path set by Django to grab the template
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('edit/<pk>', CustomUserUpdateView.as_view(), name='user-edit'),
    path('', include('pages.urls')),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('practices/', include('practice.urls')),
    path('training_sessions/', include('training_session.urls')),
    path('training_plans/', include('training_plan.urls')),
    path('players/<int:category_id>/<int:season_id>', PlayerListView.as_view(), name='players_list'),
    path('managers/<int:category_id>/<int:season_id>/', ManagerListView.as_view(), name='managers_list'),

]

# In context of dev (Debug is set) the following configuration will be applied
# Because using the django application we need to emulate a real server sttings
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
