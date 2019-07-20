from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import ugettext_lazy as _


class University(models.Model):
    title = models.CharField(max_length=255)
    leaderID = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class User(AbstractUser):
    second_name = models.CharField(max_length=50)

    untiID = models.PositiveIntegerField(db_index=True, null=True, blank=True, unique=True, )
    leaderID = models.PositiveIntegerField(db_index=True, null=True, blank=True, unique=True, )

    class Meta:
        verbose_name = _(u'Пользователь')
        verbose_name_plural = _(u'Пользователи')

    def __str__(self):
        return '%s %s' % (self.unti_id, self.get_full_name())

    @property
    def fio(self):
        return ' '.join(filter(None, [
            self.last_name, self.first_name, self.second_name]))

    def get_full_name(self):
        return ' '.join(filter(None, [self.last_name, self.first_name]))
