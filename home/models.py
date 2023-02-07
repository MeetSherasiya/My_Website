from django.db import models


# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=122)
    email = models.CharField(max_length=122)
    subject = models.CharField(max_length=200)
    message = models.TextField()
    date = models.DateField()

    def __str__(self):
        # this function will return the name of the contact in the admin panel
        title = self.name + " - " + self.email
        return title