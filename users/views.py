from django.shortcuts import render
from rest_framework.views import APIView
from .models import CustomUser, InvolvedAsICategoryForSeason
from club.models import Season
from django.views.generic import ListView, UpdateView
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import UpdateView
from django.db.models import Q
import json  # used to generate search request
import jsonify
from rest_framework import viewsets
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from users.serializers import CustomUserSerializer
from rest_framework.renderers import JSONRenderer


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

    def get_queryset(self):
        """[summary]
        Over ridded function in order to get results whatever the query is.

        Returns:
            InvolvedAsICategoryForSeason: returning a list of players belonging to a category
            for the current season according data inuput
            or all players belonging to the category for the current season if no query
        """
        # Retrieveing the both values path in the parameters
        season_id = self.kwargs["season_id"]
        category_id = self.kwargs["category_id"]

        query = self.request.GET.get('query')
        print(query)
        if query is not None:
            members = CustomUser.objects.filter(
                Q(first_name__icontains=query) | Q(last_name__icontains=query)
            )
            self.object_list = InvolvedAsICategoryForSeason.objects.filter(
                category=category_id).filter(season=season_id).filter(member__in=members).exclude(is_player=False)
        else:
            self.object_list = InvolvedAsICategoryForSeason.objects.filter(
                category=category_id).filter(season=season_id).exclude(is_player=False)  # In this case the query is empty
        return self.object_list

    def get_context_data(self):

        context = super().get_context_data()
        catid = self.kwargs["category_id"]
        context["category_id"] = catid
        # context["qs_json"] = json.dumps(list(CustomUser.objects.values()))
        return context


class ManagerListView(LoginRequiredMixin, ListView):
    model = InvolvedAsICategoryForSeason
    paginate_by = 10
    template_name = 'users/ManagersListCatSeason.html'
    success_url = 'managers_list'

    # see example at the following URL
    # https://learndjango.com/tutorials/django-search-tutorial

    def get_queryset(self):
        """[summary]
        Over ridded function in order to get results whatever the query is.

        Returns:
            InvolvedAsICategoryForSeason: returning a list of manegers belonging to a category
            for the current season according data inuput
            or all managers belonging to the category for the current season if no query
        """
        # Retrieveing the both values path in the parameters
        catid = self.kwargs["category_id"]
        seaid = self.kwargs["season_id"]
        query = self.request.GET.get('query')
        if query is not None:

            members = CustomUser.objects.filter(
                Q(first_name__icontains=query) | Q(last_name__icontains=query)
            )
            print(members)
            self.object_list = InvolvedAsICategoryForSeason.objects.filter(
                category=catid).filter(season=seaid).filter(member__in=members).exclude(is_player=True)

        else:
            self.object_list = InvolvedAsICategoryForSeason.objects.filter(
                category=catid).filter(season=seaid).exclude(is_player=True)  # In this case the query is empty
        return self.object_list

    def get_context_data(self):

        context = super().get_context_data()
        catid = self.kwargs["category_id"]
        context["category_id"] = catid
        return context


def autosuggest(request):
    query = request.GET.get('query')
    print(type(query))
    payload = []
    if query:
        members = CustomUser.objects.filter(
            Q(first_name__icontains=query) | Q(last_name__icontains=query)
        )
        for member in members:
            payload.append(member)

        serialized = CustomUserSerializer(payload, many=True)

    return JsonResponse({'status': 200, 'list': serialized.data})


# class GetMembersAPI(APIView):

#     def get(self, request):
#         members = CustomUser.objects.all()
#         serialized = CustomUserSerializer(members, many=True)
#         response = Response(serialized.data)
#         return response
