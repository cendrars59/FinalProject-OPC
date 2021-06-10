from django.shortcuts import render
from .models import CustomUser
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
    fields = ['first_name','last_name','email','username','date_of_birth',
        'address1', 'address2', 'zip_code','city', 'country',
        'mobile_phone','phone_for_whatsapp', 'about','photo', 'involed_in_categories' ]
    template_name = 'users/user_edit.html'
    
    
