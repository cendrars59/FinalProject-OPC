from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from users.models import CustomUser, Role

# Customize the admin interface in order to manage the custom user according the defined user model
class CustomUserAdminConfig(UserAdmin):
    model = CustomUser
    search_fields = ('email', 'username',)
    list_filter = ('email', 'username', 'is_active', 'is_staff')
    ordering = ('username',)
    list_display = ('email', 'username','last_name', 'first_name',
                    'is_active', 'is_staff')
    fieldsets = (
        ('Informations membre', {'fields': ('email', 'username','last_name' ,'first_name','password',)}),
        ('Informations contact membre', {'fields': ('mobile_phone', 'phone_for_whatsapp',)}),
        ('Informations club', {'fields': ('involed_in_categories',)}),
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




