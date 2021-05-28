import uuid
from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models
from club.models import Category

# Create your models here.


class Skill(models.Model):

    code = models.UUIDField(default=uuid.uuid4)
    label = models.CharField(unique=True, max_length=128)
    description = models.TextField(null=False, default="Ajoutez ici la decription de la compétence visée")
    is_active = models.BooleanField(null=False, default=True)

    def __str__(self):
        """Return the label of the object instead of technical tag.
        Returns:
            String: Name of the skill
        """
        return self.label


class Practice(models.Model):

    code = models.UUIDField(default=uuid.uuid4)
    label = models.CharField(verbose_name='Titre', max_length=255)
    description = RichTextUploadingField(verbose_name='Description', blank=True, null=True)
    #description = models.TextField(verbose_name='Description', null=True, blank=True)
    is_active = models.BooleanField(verbose_name='Activé', default=True)
    # date_posted = models.DateTimeField(default=timezone.now)
    # author = models.ForeignKey(User, on_delete=models.CASCADE)
    categories = models.ManyToManyField(Category, verbose_name='Liste des catégories')
    skills = models.ManyToManyField(Skill, verbose_name='Liste des compétences')

    class Meta:
        verbose_name = "practice"
        verbose_name_plural = "practices"

    def __str__(self):
        return self.label

    # def get_absolute_url(self):
    #     # helping to return the full path to the object according the primary key
    #     return reverse("practice-details", kwargs={"pk": self.pk})
