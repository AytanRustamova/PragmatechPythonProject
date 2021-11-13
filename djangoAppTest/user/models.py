from django.db import models


# Create your models here.


class User(models.Model):
    username = models.CharField(max_length=127, null=True, blank=True)
    email = models.TextField(help_text='Bura emailinizi daxil edin...')
    password = models.(auto_now_add=True)
    confPassword = models.CharField(max_length=63, verbose_name='Muellif', )


