from django.shortcuts import render
from .models import CustomUser, InvolvedAsICategoryForSeason
from club.models import Season
from django.views.generic import ListView, UpdateView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import UpdateView
from django.db.models import Q  # used to generate search request


class CustomUserUpdateView(LoginRequiredMixin, UpdateView):

    model = CustomUser
    fields = ['first_name', 'last_name', 'email', 'username', 'date_of_birth',
              'address1', 'address2', 'zip_code', 'city', 'country',
              'mobile_phone', 'phone_for_whatsapp', 'about', 'photo', 'has_roles_in_categories_in_clubs']
    template_name = 'users/user_edit.html'


class PlayerListView(LoginRequiredMixin, ListView):
    model = InvolvedAsICategoryForSeason
    paginate_by = 10
    template_name = 'users/PlayersListCatSeason.html'
    success_url = 'players_list'

    # see example at the following URL
    # https://learndjango.com/tutorials/django-search-tutorial

    def get_queryset(self, *args, **kwagrs):
        """[summary]
        Over ridded function in order to get results whatever the query is. 

        Returns:
            InvolvedAsICategoryForSeason: returning a list of players belonging to a category
            for the current season according data inuput
            or all players belonging to the category for the current season if no query 
        """
        # Retrieveing the both values path in the parameters
        catid = kwagrs["category_id"]
        seaid = kwagrs["season_id"]
        query = self.request.GET.get('q')
        if query is not None:

            print(query)
            object_list = InvolvedAsICategoryForSeason.objects.filter(
                Q(first_name__icontains=query) | Q(last_name__icontains=query)
            )

        else:
            self.object_list = InvolvedAsICategoryForSeason.objects.filter(
                category=catid).filter(season=seaid).exclude(is_player=False)  # In this case the query is empty
        return self.object_list

    def get(self, request, *args, **kwagrs):
        # https://newbedev.com/pass-url-argument-to-listview-queryset
        """The purpose is to get the list of players for the active season and
        the selected category for a get request

        Args:
            request ([type]): [description]
            category_id : Category id passed as argument in the url
            season_id : Season id passed as argument in the url
        Returns:
            [type]: [description]
        """
        seaid = kwagrs["season_id"]
        catid = kwagrs["category_id"]
        self.object_list = InvolvedAsICategoryForSeason.objects.filter(
            category=catid).filter(season=seaid).exclude(is_player=False)
        context = self.get_context_data()
        context["category_id"] = catid
        return self.render_to_response(context)

    # def get_context_data(self, request, **kwargs):

    #     context = super().get_context_data(**kwargs)
    #     catid = kwagrs["category_id"]

    #     context["category_id"] = catid
    #     return context


class ManagerListView(LoginRequiredMixin, ListView):
    model = InvolvedAsICategoryForSeason
    paginate_by = 10
    template_name = 'users/ManagersListCatSeason.html'
    success_url = 'managers_list'

    # see example at the following URL
    # https://learndjango.com/tutorials/django-search-tutorial

    def get_queryset(self, *args, **kwagrs):
        """[summary]
        Over ridded function in order to get results whatever the query is. 

        Returns:
            InvolvedAsICategoryForSeason: returning a list of manegers belonging to a category
            for the current season according data inuput
            or all managers belonging to the category for the current season if no query 
        """
        # Retrieveing the both values path in the parameters
        catid = kwagrs["category_id"]
        seaid = kwagrs["season_id"]
        query = self.request.GET.get('q')
        if query is not None:

            print(query)
            self.object_list = InvolvedAsICategoryForSeason.objects.filter(
                Q(first_name__icontains=query) | Q(last_name__icontains=query)
            )

        else:
            self.object_list = InvolvedAsICategoryForSeason.objects.filter(
                category=catid).filter(season=seaid).exclude(is_player=True)  # In this case the query is empty
        return self.object_list

    def get(self, request, *args, **kwagrs):
        # https://newbedev.com/pass-url-argument-to-listview-queryset
        """The purpose is to get the list of players for the active season and
        the selected category for a get request

        Args:
            request ([type]): [description]
            category_id : Category id passed as argument in the url
            season_id : Season id passed as argument in the url
        Returns:
            [type]: [description]
        """
        seaid = kwagrs["season_id"]
        catid = kwagrs["category_id"]
        self.object_list = InvolvedAsICategoryForSeason.objects.filter(
            category=catid).filter(season=seaid).exclude(is_player=True)
        context = self.get_context_data()
        context["category_id"] = catid
        return self.render_to_response(context)

    # def get_context_data(self, request, **kwargs):

    #     context = super().get_context_data(**kwargs)
    #     catid = kwagrs["category_id"]

    #     context["category_id"] = catid
    #     return context
