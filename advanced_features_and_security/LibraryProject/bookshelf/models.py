
from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    publication_year = models.IntegerField()

    def __str__(self):
        return f"{self.title} by {self.author} ({self.publication_year})"




from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.utils.translation import gettext_lazy as _

class CustomUserManager(BaseUserManager):
    def create_user(self, username, email, password=None, **extra_fields):
        if not email:
            raise ValueError(_('The Email field must be set'))
        email = self.normalize_email(email)
        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True.'))

        return self.create_user(username, email, password, **extra_fields)

class CustomUser(AbstractUser):
    date_of_birth = models.DateField(null=True, blank=True, verbose_name='Date of Birth')
    profile_photo = models.ImageField(upload_to='profile_photos/', null=True, blank=True, verbose_name='Profile Photo')
    email = models.EmailField(_('email address'), unique=True)

    objects = CustomUserManager()

    def __str__(self):
        return self.username
    

    class Book(models.Model):
        title = models.CharField(max_length=200)
        author = models.CharField(max_length=200)
        publication_date = models.DateField(default = '2020-01-01')
        modified_by = models.ForeignKey()

#Extending Book Model with Custom Permissions
    class Meta:
        permissions =(
            ('can_create', 'Can create'),
            ('can_view', 'Can view'),
            ('can_edit', 'Can edit'),
            ('can_delete', 'Can delete'),

        )

    def _str_(self):
        return f"{self.title} by {self.author} published on {self.publication_date}"



    class Meta:
        permissions = [
            ('can_view', 'Can view'),
            ('can_create', 'Can create'),
            ('can_edit', 'Can edit'),
            ('can_delete', 'Can delete'),
        ]