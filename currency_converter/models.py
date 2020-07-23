# from django.db import models
# from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
# from django.template.defaultfilters import slugify


# class AccountManager(BaseUserManager):
#     def create_user(self, email, password=None, **kwargs):
#         if not email:
#             raise ValueError('Users must have a valid email address.')

#         if not kwargs.get('username'):
#             raise ValueError('Users must have a valid username.')

#         account = self.model(
#             email=self.normalize_email(email), username=kwargs.get('username')
#         )

#         account.set_password(password)
#         account.save()

#         return account

#     def create_superuser(self, email, password, **kwargs):
#         account = self.create_user(email, password, **kwargs)

#         account.is_admin = True
#         account.is_active = True
#         account.is_staff = True
#         account.save()

#         return account

# class Account(AbstractBaseUser):
#     email = models.EmailField(unique=True)
#     username = models.CharField(max_length=40, unique=True)
#     slug = models.SlugField(max_length=60)

#     is_staff = models.BooleanField(default=False)
#     is_active = models.BooleanField(default=False)
#     is_admin = models.BooleanField(default=False)

#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now_add=True)

#     objects = AccountManager()

#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = ['username']

#     def save(self, *args, **kwargs):

#         self.slug = slugify(self.username)

#         super(Account, self).save(*args, **kwargs)

#     def __str__(self):
#         return self.email

#     def get_full_name(self):
#         return self.name