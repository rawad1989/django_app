from django.utils.translation import gettext_lazy as _
from django.db import models
from django.contrib.auth.models import PermissionsMixin, BaseUserManager
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.validators import UnicodeUsernameValidator


class UserManager(BaseUserManager):
    def create_user(self, username, email, password):
        user = self.model(
            username=username,
            email=email,
            password=password,
            is_staff=False,
            is_superuser=False,
        )

        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, username, email, password):
        user = self.model(
            username=username,
            email=email,
            password=password,
            is_superuser=True,
            is_staff=True,
        )

        user.set_password(password)
        user.save()
        return user


class User(AbstractBaseUser, PermissionsMixin):
    username_validator = UnicodeUsernameValidator()
    username = models.CharField(
        _('username'),
        max_length=150,
        unique=True,
        validators=[username_validator],
    )
    email = models.EmailField(_('Email Address'), blank=True)
    is_staff = models.BooleanField(
        _('Is Staff'),
        default=False,
        help_text=_('Designates whether the user can log into this admin site.'),
    )
    is_active = models.BooleanField(
        _('Is Active'),
        default=True,
        help_text=_(
            'Designates whether this user should be treated as active.'
        ),
    )
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    objects = UserManager()

    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

    def clean(self):
        super().clean()
        self.email = self.__class__.objects.normalize_email(self.email)

    def get_full_name(self):
        """Return the full name for the user."""
        return self.username

    def get_short_name(self):
        """Return the short name for the user."""
        return self.username

    def email_user(self, subject, message, from_email=None, **kwargs):
        """Send an email to this user."""
        pass
