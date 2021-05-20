from django.contrib import admin
from .models import Club, Team, Category, Division, Season, EventType, CategoryClubBySeason

# Register your models here.


class CategoryAdmin(admin.ModelAdmin):
    pass


admin.site.register(Category, CategoryAdmin)


class SeasonAdmin(admin.ModelAdmin):
    pass


admin.site.register(Season, SeasonAdmin)


class ClubAdmin(admin.ModelAdmin):
    pass


admin.site.register(Club, ClubAdmin)


class TeamAdmin(admin.ModelAdmin):
    pass


admin.site.register(Team, TeamAdmin)


class DivisionAdmin(admin.ModelAdmin):
    pass


admin.site.register(Division, DivisionAdmin)


class EventTypeAdmin(admin.ModelAdmin):
    pass


admin.site.register(EventType, EventTypeAdmin)


class CategoryClubBySeasonAdmin(admin.ModelAdmin):
    pass


admin.site.register(CategoryClubBySeason, CategoryClubBySeasonAdmin)
