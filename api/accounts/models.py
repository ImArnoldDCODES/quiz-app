from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, UserManager
import uuid


class BaseModel(models.Model):
    id = models.UUIDField(
        primary_key=True, max_length=36, default=uuid.uuid4, editable=False
    )
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True


class User(BaseModel, AbstractBaseUser, PermissionsMixin):

    first_name = models.CharField(max_length=255, blank=True)
    last_name = models.CharField(max_length=255, blank=True)
    username = models.CharField(max_length=200, blank=False, unique=True)
    email = models.EmailField(max_length=255, blank=False, unique=True)
    updated = models.DateTimeField(auto_now=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    REQUIRED_FIELDS = ["email"]
    USERNAME_FIELD = "username"

    objects = UserManager()

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"

    def __str__(self):
        return self.username
