from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from users.models import CustomUser, Role, InvolvedAsICategoryForSeason

# Customize the admin interface in order to manage the custom user according the defined user model
class CustomUserAdminConfig(UserAdmin):
    model = CustomUser
    search_fields = ('email', 'username',)
    
    ordering = ('username',)
    list_display = ('email', 'username','last_name', 'first_name',
                    'is_active', 'is_staff')
    fieldsets = (
        ('Informations membre', {'fields': ('email', 'username','last_name' ,'first_name','password',)}),
        ('Informations contact membre', {'fields': ('mobile_phone', 'phone_for_whatsapp',)}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
        ('Informations complémentaires', {'fields': ('about','photo')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'username', 'first_name', 'password1', 'password2', 'is_active', 'is_staff')}
         ),
    )


admin.site.register(CustomUser, CustomUserAdminConfig)


class RoleAdmin(admin.ModelAdmin):
    pass


admin.site.register(Role, RoleAdmin)


class InvolvedAsICategoryForSeasonAdmin(admin.ModelAdmin):
    model = InvolvedAsICategoryForSeason
    search_fields = ('club', 'season', 'role', 'member',)
    list_filter = ('club', 'season', 'role', 'member', 'license_is_paid')
    list_display = ('club', 'season','category' ,'role', 'member', 'license_is_paid')


admin.site.register(InvolvedAsICategoryForSeason, InvolvedAsICategoryForSeasonAdmin)




