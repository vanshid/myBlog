from django.db import models

# Create your models here.
class ConnectModel(models.Model):
    firstname = models.CharField(max_length=15)
    lastname = models.CharField(max_length=15)
    email = models.EmailField(max_length=254)

    def __str__(self):
        return {self.fname},{self.lname},{self.email}
    