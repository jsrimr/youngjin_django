from django.db import models
from django.contrib import auth

from django.contrib.auth.models import (BaseUserManager, AbstractBaseUser, PermissionsMixin)
from django.contrib.auth import get_user_model

# Create your models here.

# class User(auth.models.User, auth.models.PermissionsMixin):
#     def __str__(self):
#         return "@{}".format(self.username)


class UserManager(BaseUserManager):
    def create_user(self, dpt, dpt_code, password=None):
        if not dpt:
            raise ValueError('Users must have an id')

        user = self.model(
            dpt= dpt,
            dpt_code=dpt_code,
        )
        user.set_password(password)
        user.is_admin = False
        user.is_active = True
        user.save(using=self._db)
        return user

    def create_superuser(self, dpt, dpt_code, password):
        user = self.create_user(
            dpt = dpt,
            password=password,
            dpt_code=dpt_code,
        )
        user.is_admin = True
        user.is_active = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser,PermissionsMixin):
    dpt = models.CharField(
        verbose_name='dpt',
        max_length=255,
        unique=True,
        default= ''
    )
    dpt_code = models.CharField(max_length=255,unique=False, default = '')
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'dpt'
    REQUIRED_FIELDS = ['dpt_code']

    def __str__(self):
        return self.dpt

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin