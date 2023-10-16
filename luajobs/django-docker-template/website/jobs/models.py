from django.db import models

# Create your models here.


from django.db import models

# Create your models here.


class User(models.Model):
    first_name = models.CharField(max_length=200)
    second_name = models.CharField(max_length=200)
    email = models.EmailField()
    last_login = models.DateTimeField()


class Jobs(models.model):
    description = models.CharField(max_length=2000)
    type = models.CharField(max_length=100) # remote/hybrid/onsite
    date_of_post = models.DateTimeField()
    conatct_email = models.EmailField()