<<<<<<< HEAD
=======
from unittest.util import _MAX_LENGTH
>>>>>>> 8bbdaef (login page)
from django.db import models

class User(models.Model):
    username = models.CharField(max_length = 20, verbose_name = 'Username')
    first_name = models.CharField(max_length = 20, verbose_name = 'First name')
    email = models.EmailField(verbose_name = 'Email')
    password = models.CharField(max_length = 20, verbose_name = 'Password')
<<<<<<< HEAD
    # repeat_password = models.CharField(max_length = 20, verbose_name = 'Repeat passord')
    # is_agree = models.BooleanField()

    def __str__(self):
        return self.username
=======
    repeat_password = models.CharField(max_length = 20, verbose_name = 'Repeat passord')
    is_agree = models.BooleanField()
>>>>>>> 8bbdaef (login page)

    class Meta:
        db_table = 'user'