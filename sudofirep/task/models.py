
from django.db import models

class User(models.Model):

    first_name=models.CharField(max_length=200)
    last_name=models.CharField(max_length=200)
    email=models.CharField(max_length=200,null=False,unique=True,)
    mobile_no=models.IntegerField(null=False,unique=True,)


class Customer(models.Model):
    profile_number=models.IntegerField()
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    def __str__(self):
        return self.profile_number    


