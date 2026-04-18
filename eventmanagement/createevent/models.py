from django.db import models

from account.models import Account


class Room(models.Model):
    roomID = models.AutoField(primary_key=True)
    roomName = models.CharField(max_length=100)

    def __str__(self):
        return self.roomName


class Event(models.Model):
    eventID = models.AutoField(primary_key=True)
    eventTitle = models.CharField(max_length=100)
    dateOfEvent = models.DateField()
    maxParticipants = models.IntegerField()
    room = models.ForeignKey(Room, on_delete=models.RESTRICT)

    def __str__(self):
        return self.eventTitle


class Attends(models.Model):
    username = models.ForeignKey(Account, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    status = models.CharField(max_length=20)
    dateRegistered = models.DateField()

    class Meta:
        unique_together = ('username', 'event')