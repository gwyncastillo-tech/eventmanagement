from django.db import models

class Account(models.Model):
    USER_TYPE = (
        (1, 'User'),
        (0, 'Responder'),
    )

    username = models.CharField(max_length=50, primary_key=True)
    email = models.EmailField()
    password = models.CharField(max_length=50)

    fullname = models.CharField(max_length=100)
    dob = models.DateField(null=True, blank=True)
    address = models.CharField(max_length=255, null=True, blank=True)
    phone = models.CharField(max_length=20, null=True, blank=True)

    type = models.IntegerField(choices=USER_TYPE, default=1)

    def __str__(self):
        return self.fullname