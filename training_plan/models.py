from tkinter import CASCADE
from tracemalloc import is_tracing
from django.db import models
import uuid
from ckeditor_uploader.fields import RichTextUploadingField
from club.models import Category
from training_session.models import TrainingSession
from users.models import CustomUser
from datetime import datetime


class TrainingPlan(models.Model):
    
    code = models.UUIDField(default=uuid.uuid4)
    label = models.CharField(verbose_name='Titre', max_length=255)
    description = RichTextUploadingField(verbose_name='Description', blank=True, null=True)
    category = models.OneToOneField(Category, verbose_name='Catégorie', blank=True, null=False,on_delete=models.CASCADE)
    training_session = models.OneToOneField(TrainingSession, verbose_name='Session de référence',
     blank=True, null=True, on_delete=models.CASCADE)
    required_materials = models.CharField(verbose_name='Liste de materiel', max_length=1024, blank=True, null=True)
    start_date_time = models.DateTimeField(verbose_name='Date et heure de début', default=datetime.now)
    duration_in_minutes = models.IntegerField(blank=True, null=True)
    debriefing = RichTextUploadingField(verbose_name='Debriefing', blank=True, null=True)
    is_canceled = models.BooleanField(default=False, null=True)
    attenders_list = models.ManyToManyField(CustomUser, verbose_name='Liste des participants', through='TrainingPlanAttendersList') 
    class Meta:
        verbose_name = "training_plan"
        verbose_name_plural = "training_plans"

    def __str__(self):
        return self.label


class TrainingPlanAttendersList(models.Model):
    training_session_plan = models.ForeignKey(TrainingPlan,null=False, on_delete=models.CASCADE)
    attender = models.ForeignKey(CustomUser,null=False, on_delete=models.CASCADE)
    will_attend = models.BooleanField(null=False, default=True)
    off_justified = models.BooleanField(null=False, default=True)
    has_attended = models.BooleanField(null=False, default=False)
    is_staff = models.BooleanField(null=False, default=False)

    class Meta:
        unique_together = [['training_session_plan', 'attender']]
