from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractUser
from django.utils.translation import ugettext as _

from utils.choices import STATUS_CHOICES
from utils.validators import validate_birth_date

class UserManager(BaseUserManager):

    def create_user(self, username, date_of_birth, nationality,
                    first_name=None, middle_name=None, last_name=None,
                    email=None, password=None):
        """
        Creates and saves a User with the given date of
        birth and password.
        """

        if not date_of_birth:
            raise ValueError('Users must have a birth date')

        user = self.model(
            date_of_birth=date_of_birth,
            username=username,
            first_name=first_name,
            middle_name=middle_name,
            last_name=last_name,
            email=email,
            nationality=nationality
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, date_of_birth, nationality,
                         first_name, last_name, email, password):
        """
        Creates and saves a superuser with the given date of birth and password.
        """

        user = self.create_user(password=password,
            date_of_birth=date_of_birth,
            username=username,
            nationality=nationality,
            first_name=first_name,
            last_name=last_name,
            email=email,
        )
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user

class UserProfile(AbstractUser):
    """
    Class representing an user.
    """

    middle_name = models.CharField(_('Middle Name'), max_length=30, blank=True,
                                  null=True)

    profile_pic = models.ImageField(_('Profile Picture'), null=True, blank=True,
                                    upload_to='%Y/%m/%d')

    date_of_birth = models.DateField(_('Date of birth'), null=False,
                                    blank=False, validators=[validate_birth_date])

    nationality = models.CharField(_('Nationality'), max_length=40, blank=True,
                                  null=True)

    status = models.CharField(_('Status'), max_length=1, null=False,
                              blank=False, default='A', choices=STATUS_CHOICES)

    REQUIRED_FIELDS = ['date_of_birth', 'nationality', 'first_name',
                       'last_name', 'email']

    objects = UserManager()

    class Meta:
        db_table = 'pm_user'
        verbose_name_plural = 'Users'
