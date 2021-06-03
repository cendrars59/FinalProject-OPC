from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django.core.validators import RegexValidator
from django.utils.translation import gettext_lazy as _ # About https://docs.djangoproject.com/fr/3.2/topics/i18n/translation/
from django_countries.fields import CountryField # About https://pypi.org/project/django-countries/
from django.core import validators
from django.db import models

class UserManager(BaseUserManager):
    
    def create_user(self, email, username, password , **other_fields):
    # Method to manage user creation according the new fields
    # not belonging to the orginal user model (Provided by Django)

        if not email:
            raise ValueError(_('Vous devez fournir un email'))

        email = self.normalize_email(email)
        user = self.model(email=email, username=username,**other_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, username, password , **other_fields):
        
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


class User(AbstractBaseUser, PermissionsMixin):

    # Email field that serves as the username field
    email = models.CharField(
        max_length = 50, 
        unique = True, 
        validators = [validators.EmailValidator()],
        verbose_name = "Email"
    )

    username = models.CharField(
        max_length = 50,
        verbose_name = "Nom utilisateur",
        unique = True
    )


    first_name = models.CharField(
        max_length = 50,
        verbose_name = "Prénom Name",
    )

    last_name = models.CharField(
        max_length = 50,
        verbose_name = "Nom",
    )

    date_of_birth = models.DateField(
        verbose_name=_("Date of birth"),
        blank=True,
        null=True)

    address1 = models.CharField(
        verbose_name=_("Addresse ligne 1"),
        max_length=1024,
        blank=True,
        null=True)

    address2 = models.CharField(
        verbose_name=_("Addresse ligne 2"),
        max_length=1024,
        blank=True,
        null=True)

    zip_code = models.CharField(
        verbose_name=_("Postal Code"),
        max_length=12,
        blank=True,
        null=True)

    city = models.CharField(
        verbose_name=_("City"),
        max_length=1024,
        blank=True,
        null=True)

    country = CountryField(
        blank=True,
        null=True)

    phone_regex = RegexValidator(
        regex=r"^\+(?:[0-9]●?){6,14}[0-9]$",
        message=_("Enter a valid international mobile phone number starting with +(country code)"))

    mobile_phone = models.CharField(
        validators=[phone_regex],
        verbose_name=_("Téléphone mobile"),
        max_length=17,
        blank=True,
        null=True)

    phone_for_whatsapp = models.BooleanField(
        verbose_name=_("A utiliser pour WhatsApp"),
        default=False)

    additional_information = models.CharField(
        verbose_name=_("Information complémentaires"),
        max_length=4096,
        blank=True,
        null=True)

    # photo = models.ImageField(
    #     verbose_name=_("Photo du membre"),
    #     upload_to='photos/',
    #     default='photos/default-user-avatar.png')

    # Other required fields for authentication
    # If the user is a staff, defaults to false
    is_staff = models.BooleanField(default=False)

    # If the user account is active or not. Defaults to True.
    # If the value is set to false, user will not be allowed to sign in.
    is_active = models.BooleanField(default=True)
    
    
    def get_full_name(self):
        # Returns the first_name and the last_name
        return f'{self.first_name} {self.last_name}'

    def get_short_name(self):
        # Returns the short name for the user.
        return self.first_name

    def __string__(self):
        # Returns the short name for the user.
        return self.username
    

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    objects = UserManager()
