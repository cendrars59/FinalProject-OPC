from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django.core.validators import RegexValidator
from django_countries.fields import CountryField  # About https://pypi.org/project/django-countries/
from django.core import validators
from django.db import models
from club.models import Season, Club, Category
import uuid


class CustomUserManager(BaseUserManager):

    def create_superuser(self, email, username, password, **other_fields):

        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)
        other_fields.setdefault('is_active', True)

        if other_fields.get('is_staff') is not True:
            raise ValueError(
                'Superuser must be assigned to is_staff=True.')
        if other_fields.get('is_superuser') is not True:
            raise ValueError(
                'Superuser must be assigned to is_superuser=True.')

        return self.create_user(email, username, password, **other_fields)

    def create_user(self, email, username, password, **other_fields):

        if not email:
            raise ValueError('Vous devez fournir un email')

        email = self.normalize_email(email)
        user = self.model(email=email, username=username,
                          **other_fields)
        user.set_password(password)
        user.save()
        return user


class Role(models.Model):

    code = models.UUIDField(default=uuid.uuid4)
    label = models.CharField(unique=True, max_length=128)
    description = models.TextField(null=True, default="Ajoutez ici la decription du rôle")
    is_active = models.BooleanField(null=False, default=True)
    is_manager = models.BooleanField(null=False, default=False)
    is_player = models.BooleanField(null=False, default=False)

    @classmethod
    def get_player_role(cls):
        player_role = cls.objects.get(is_player=True)
        return player_role

    def __str__(self):
        """Return the label of the object instead of technical tag.
        Returns:
            String: Name of the role
        """
        return self.label


class CustomUser(AbstractBaseUser, PermissionsMixin):

    # Email field that serves as the username field
    email = models.EmailField(
        max_length=100,
        unique=True,
        validators=[validators.EmailValidator()],
        verbose_name="Email"
    )

    username = models.CharField(
        max_length=50,
        verbose_name="Nom utilisateur",
        unique=True
    )

    first_name = models.CharField(
        max_length=50,
        verbose_name="Prénom",
    )

    last_name = models.CharField(
        max_length=50,
        verbose_name="Nom",
    )

    date_of_birth = models.DateField(
        verbose_name="Date de naissance",
        blank=True,
        null=True)

    address1 = models.CharField(
        verbose_name="Addresse ligne 1",
        max_length=1024,
        blank=True,
        null=True)

    address2 = models.CharField(
        verbose_name="Addresse ligne 2",
        max_length=1024,
        blank=True,
        null=True)

    zip_code = models.CharField(
        verbose_name="Code postal",
        max_length=12,
        blank=True,
        null=True)

    city = models.CharField(
        verbose_name="Ville",
        max_length=1024,
        blank=True,
        null=True)

    country = CountryField(
        verbose_name="Pays",
        blank=True,
        null=True)

    phone_regex = RegexValidator(
        regex=r"^\+(?:[0-9]●?){6,14}[0-9]$",
        message="Entrer un code international pour mobile commençant par +(country code) par +336")

    mobile_phone = models.CharField(
        validators=[phone_regex],
        verbose_name="Téléphone mobile",
        max_length=17,
        blank=True,
        null=True)

    phone_for_whatsapp = models.BooleanField(
        verbose_name="A utiliser pour WhatsApp",
        default=False)

    about = models.TextField(
        verbose_name="Information complémentaires",
        blank=True,
        null=True)

    photo = models.ImageField(
        verbose_name="Photo du membre",
        upload_to='member_photos/',
        default='photos/default-user-avatar.png')

    # to restrict the application to only people having framing function in the club
    is_club_manager = models.BooleanField(default=False)

    # Other required fields for authentication
    # If the user is a staff, defaults to false
    is_staff = models.BooleanField(default=False)

    # If the user account is active or not. Defaults to True.
    # If the value is set to false, user will not be allowed to sign in.
    is_active = models.BooleanField(default=True)

    has_roles_in_categories_in_clubs = models.ManyToManyField(
        Club, blank=True, null=True, through='InvolvedAsICategoryForSeason')
    seasons = models.ManyToManyField(Season, blank=True, null=True, through='InvolvedAsICategoryForSeason')
    categories = models.ManyToManyField(Category, blank=True, null=True, through='InvolvedAsICategoryForSeason')
    roles = models.ManyToManyField(Role, blank=True, null=True, through='InvolvedAsICategoryForSeason')

    objects = CustomUserManager()

    def get_full_name(self):
        # Returns the first_name and the last_name
        return f'{self.first_name} {self.last_name}'

    def get_short_name(self):
        # Returns the short name for the user.
        return self.first_name

    def __string__(self):
        user = f"{self.first_name} - {self.last_name}"
        return user

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'password']

    # def has_perm(self, perm, obj=None):
    #     return True

    # def has_module_perms(self, app_label):
    #     return True

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('user-edit', kwargs={'pk': self.pk})


class InvolvedAsICategoryForSeason(models.Model):
    club = models.ForeignKey(Club, null=True, on_delete=models.CASCADE)
    season = models.ForeignKey(Season, null=True, verbose_name='Saison', on_delete=models.CASCADE)
    member = models.ForeignKey(CustomUser, null=True, verbose_name='Membre', on_delete=models.CASCADE)
    category = models.ForeignKey(Category, null=True, verbose_name='Catégorie', on_delete=models.CASCADE)
    role = models.ForeignKey(Role, null=True, on_delete=models.CASCADE)
    license_number = models.TextField(verbose_name='Numéro de licence',
                                      null=True, default="Non défine")
    license_is_paid = models.BooleanField(verbose_name='License payée', default=False)
    is_active = models.BooleanField(null=False, default=True)
    is_player = models.BooleanField(null=False, default=True)

    def __string__(self):
        name = f"{self.club} - {self.season} - {self.member} - {self.category}"
        return name

    class Meta:
        unique_together = [['club', 'season', 'member', 'category', 'role']]

    @classmethod
    def get_user_categories_for_a_season(cls, user, season):
        '''
        retrieve all the categories where the current user is involved for the 
        current season
        '''
        user_categories = cls.objects.filter(season=season).filter(member=user)
        return user_categories
