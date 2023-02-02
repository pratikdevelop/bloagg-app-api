from django.db import models
from django.contrib.auth.models import (BaseUserManager, AbstractBaseUser)
from django.utils.timezone import now

class MyUserManager(BaseUserManager):
    def create_user(self, email, first_name, last_name,mobile, password):
        if not email:
            raise ValueError('Users must have an email')


        user = self.model( email=self.normalize_email(email), first_name=first_name, last_name = last_name, mobile=mobile)

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, first_name, last_name,mobile, password):
        user = self.create_user(email, first_name=first_name, last_name = last_name, mobile=mobile,password=password)
        user.is_admin = True
        user.save(using=self._db)
        return user

class MyUser(AbstractBaseUser):
    email = models.EmailField( verbose_name='Email', max_length=255, unique=True)
    mobile= models.IntegerField()
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=300)
    password = models.CharField( max_length=255)
    createdAt = models.DateTimeField(default=now, blank=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    objects = MyUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name','password', 'mobile']

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return self.is_admin

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin
