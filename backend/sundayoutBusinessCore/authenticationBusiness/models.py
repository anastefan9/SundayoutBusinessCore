from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class UserRole(models.TextChoices):
    admin = 'admin', 'admin'
    staff = 'staff', 'staff'
    chef = 'chef', 'chef'

class UserManager(BaseUserManager):
    def create_user(self, email, firstName, lastName, role, password=None):
        if not email:
            raise ValueError('Users must have an email address')
        
        user = self.model(
            email=self.normalize_email(email),
            firstName=firstName,
            lastName=lastName,
            role = role,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user


# Create your models here.
class User(AbstractBaseUser):
    id = models.AutoField(primary_key=True)
    firstName = models.CharField(max_length=30)
    lastName = models.CharField(max_length=30)
    email = models.EmailField(unique=True)
    role = models.CharField(max_length=5, choices=UserRole.choices, default=UserRole.staff)
    createdAt = models.DateTimeField(auto_now_add=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['firstName', 'lastName']

    def __str__(self):
        return self.email
