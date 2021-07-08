from django.db import models
import uuid
from ckeditor_uploader.fields import RichTextUploadingField
from club.models import Category
from practice.models import Practice, Skill


class TrainingSession(models.Model):
    
    code = models.UUIDField(default=uuid.uuid4)
    label = models.CharField(verbose_name='Titre', max_length=255)
    description = RichTextUploadingField(verbose_name='Description', blank=True, null=True)
    is_active = models.BooleanField(verbose_name='Activé', default=True)
    categories = models.ManyToManyField(Category, verbose_name='Liste des catégories', blank=True, null=True)
    skills = models.ManyToManyField(Skill, verbose_name='Liste des compétences', blank=True, null=True)
    practices = models.ManyToManyField(Practice, verbose_name='Liste des exercices', blank=True, null=True)
    minimum_number_of_people = models.IntegerField(blank=True, null=True)
    required_materials = models.CharField(verbose_name='Liste de materiel', max_length=1024, blank=True, null=True)

    class Meta:
        verbose_name = "training_session"
        verbose_name_plural = "training_sessions"

    def __str__(self):
        return self.label
