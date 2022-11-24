from django.db import models

class User(models.Model):
    username = models.CharField(max_length = 20, verbose_name = 'Username')
    first_name = models.CharField(max_length = 20, verbose_name = 'First name')
    email = models.EmailField(verbose_name = 'Email')
    password = models.CharField(max_length = 20, verbose_name = 'Password')
    # repeat_password = models.CharField(max_length = 20, verbose_name = 'Repeat passord')
    # is_agree = models.BooleanField()

    def __str__(self):
        return self.username

    class Meta:
        db_table = 'user'