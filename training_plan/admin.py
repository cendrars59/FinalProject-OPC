from django.contrib import admin
from training_plan.models import TrainingPlan

class TrainingPlanAdmin(admin.ModelAdmin):
    pass


admin.site.register(TrainingPlan, TrainingPlanAdmin)

# Register your models here.
