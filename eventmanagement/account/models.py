from django.db import models


class Account(models.Model):
    user_type = (('S', 'Student'), ('T', 'Teacher'))

    username = models.CharField(max_length=15, primary_key=True)
    password = models.CharField(max_length=10)
    firstname = models.CharField(max_length=50)
    middlename = models.CharField(max_length=50, null=True)
    lastname = models.CharField(max_length=50)
    type = models.CharField(max_length=1, choices=user_type)

    def __str__(self):
        return self.firstname + ' ' + self.lastname


class Student(models.Model):
    username = models.CharField(max_length=15)
    password = models.CharField(max_length=10)
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    course = models.CharField(max_length=50)
    department = models.CharField(max_length=50)

    def __str__(self):
        return self.firstname


class Teacher(models.Model):
    user = models.OneToOneField(Account, on_delete=models.CASCADE)
    specialization = models.CharField(max_length=50)
    age = models.IntegerField()

    class Meta:
        unique_together = ['specialization', 'user']

    def __str__(self):
        return self.user.firstname