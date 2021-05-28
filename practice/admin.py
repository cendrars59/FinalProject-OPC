from django.contrib import admin
from .models import Practice, Skill

# Register your models here.


class PracticeAdmin(admin.ModelAdmin):
    pass


admin.site.register(Practice, PracticeAdmin)


class SkillAdmin(admin.ModelAdmin):
    pass


admin.site.register(Skill, SkillAdmin)
