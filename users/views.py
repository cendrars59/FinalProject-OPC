from django.shortcuts import render
from .models import CustomUser, InvolvedAsICategoryForSeason
from club.models import Season
from django.views.generic import ListView, UpdateView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import UpdateView


# @login_required
# def update_user(request):

#     template_name ='users/user_edit.html'

#     if request.method == 'POST':
#         u_form = UpdateUserForm(request.POST, instance=request.user)
#         #cu_form = CustomUserUpdateForm(request.POST, request.FILES,
#         #instance=request.user.user)
#         if u_form.is_valid():
#             u_form.save()
#             #cu_form.save()
#     else:
#         print("Trop con cherche un peu")
#         u_form = UpdateUserForm(instance=request.user)
#         #cu_form = CustomUserUpdateForm(instance=request.user.user)

#     context = {
#         'u_form': u_form,
#         #'cu_form': cu_form
#     }

#     return render(request, template_name, context)


class CustomUserUpdateView(LoginRequiredMixin, UpdateView):

    model = CustomUser
    fields = ['first_name', 'last_name', 'email', 'username', 'date_of_birth',
              'address1', 'address2', 'zip_code', 'city', 'country',
              'mobile_phone', 'phone_for_whatsapp', 'about', 'photo', 'has_roles_in_categories_in_clubs']
    template_name = 'users/user_edit.html'

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)
        current_season = Season.get_active_season()
        print(current_season.label)
        context["active_season"] = Season.get_active_season()
        return context


class PlayerListView(LoginRequiredMixin, ListView):
    model = InvolvedAsICategoryForSeason
    paginate_by = 10
    template_name = 'users/PlayersListCatSeason.html'

    # see example at the following URL
    # https://learndjango.com/tutorials/django-search-tutorial

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)
        context["active_season"] = Season.get_active_season()
        return context

    def get_queryset(self, *args, **kwagrs):
        """[summary]
        Over ridded function in order to get results whatever the query is. 

        Returns:
            InvolvedAsICategoryForSeason: returning a list of players belonging to a category
            for the current season according data inuput
            or all players belonging to the category for the current season if no query 
        """
        seaid = kwagrs["season_id"]
        catid = kwagrs["category_id"]

        if catid is not None:

            print("totor")
            # object_list = InvolvedAsICategoryForSeason.objects.filter(
            #     Q(label__icontains=query) | Q(description__icontains=query)
            # )

        else:
            object_list = InvolvedAsICategoryForSeason.objects.all()  # In this case the query is empty
        return object_list

    def get(self, request, *args, **kwagrs):
        seaid = kwagrs["season_id"]
        catid = kwagrs["category_id"]
        self.object_list = InvolvedAsICategoryForSeason.objects.filter(
            category=catid).filter(season=seaid)

        # in both cases
        print(self.object_list)
        context = self.get_context_data()
        return self.render_to_response(context)
