from django.db import models
from django.db.models.expressions import F
from django.utils.translation import get_language_bidi

# Create your models here.


class Category(models.Model):

    code = models.CharField(null=False, unique=True, max_length=32)
    label = models.CharField(null=True, max_length=128)
    description = models.TextField(null=True, default="Ajoutez ici la decription de la catégorie")
    tag = models.CharField(max_length=128, default='A définir')
    is_active = models.BooleanField(null=False, default=True)
    # missing for the moment the logo of the catgegory

    def __str__(self):
        """Return the label of the object instead of technical tag.
        Returns:
            String: Name of the category
        """
        return self.label


class Season(models.Model):

    code = models.CharField(null=False, unique=True, max_length=64)
    label = models.CharField(null=True, max_length=128)
    description = models.TextField(null=True, default="Ajoutez ici la decription de las saison")
    yob = models.IntegerField()
    yoe = models.IntegerField()
    is_active = models.BooleanField(null=False, default=True)
    is_current = models.BooleanField(null=False, default=False)

    def __str__(self):
        """Return the label of the object instead of technical tag.
        Returns:
            String: Name of the season
        """
        return self.label


class Club(models.Model):
    code = models.CharField(unique=True, max_length=32)
    label = models.CharField(unique=True, max_length=128)
    description = models.TextField(null=True, default="Ajoutez ici la decription de la catégorie")
    is_active = models.BooleanField(null=False, default=True)
    is_main = models.BooleanField(null=False, default=False)
    address = models.CharField(max_length=1024)
    main_phone = models.CharField(max_length=10)
    main_email = models.CharField(unique=True, max_length=128)
    main_contact = models.CharField(unique=True, max_length=128)
    main_color_code = models.CharField(max_length=10)
    categories = models.ManyToManyField(Category, through='CategoryClubBySeason')
    seasons = models.ManyToManyField(Season, through='CategoryClubBySeason')
    # logo

    def __str__(self):
        """Return the label of the object instead of technical tag.
        Returns:
            String: Name of the Club
        """
        return self.label


class CategoryClubBySeason(models.Model):
    club = models.ForeignKey(Club, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    season = models.ForeignKey(Season, on_delete=models.CASCADE)
    label = models.CharField(unique=True, max_length=128)
    description = models.TextField(null=True, default="Ajoutez ici la decription de la catégorie")
    is_active = models.BooleanField(null=False, default=True)
    is_current = models.BooleanField(null=False, default=False)

    class Meta:
        unique_together = [['club', 'category', 'season']]

    def __str__(self):
        """Return the label of the object instead of technical tag.
        Returns:
            String: Name of the ClubSeason
        """
        return self.label


# class Role(models.Model):  To move in model members
#
#    code = models.CharField(unique=True, max_length=32)
#    label = models.CharField(unique=True, max_length=128)
#    description = models.TextField(null=True, default="Ajoutez ici la decription du rôle")
#    is_active = models.BooleanField(null=False, default=True)
    # missing for the moment the logo of the catgegory

#    def __str__(self):
#        """Return the label of the object instead of technical tag.
#        Returns:
#            String: Name of the role
#        """
#        return self.label


class EventType(models.Model):

    code = models.CharField(unique=True, max_length=32)
    label = models.CharField(unique=True, max_length=128)
    description = models.TextField(null=True, default="Ajoutez ici la decription du rôle")
    color_code = models.CharField(max_length=32)
    is_active = models.BooleanField(null=False, default=True)

    def __str__(self):
        """Return the label of the object instead of technical tag.
        Returns:
            String: Name of the event type
        """
        return self.label


class Division(models.Model):

    code = models.CharField(unique=True, max_length=32)
    label = models.CharField(unique=True, max_length=128)
    description = models.TextField(null=True, default="Ajoutez ici la decription de la division")
    is_active = models.BooleanField(null=False, default=True)

    def __str__(self):
        """Return the label of the object instead of technical tag.
        Returns:
            String: Name of the division
        """
        return self.label


class Team(models.Model):

    code = models.CharField(unique=True, max_length=32)
    label = models.CharField(unique=True, max_length=128)
    description = models.TextField(null=True, default="Ajoutez ici la decription de la division")
    is_active = models.BooleanField(null=False, default=True)
    rank = models.IntegerField(null=False, default=1)

    def __str__(self):
        """Return the label of the object instead of technical tag.
        Returns:
            String: Name of the team
        """
        return self.label


# WhatsApp group
