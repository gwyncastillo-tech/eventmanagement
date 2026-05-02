from django.db import models
from account.models import Account


class Emergency(models.Model):
    emergencyID = models.AutoField(primary_key=True)
    user = models.ForeignKey(Account, on_delete=models.CASCADE)

    title = models.CharField(max_length=100)
    description = models.TextField()

    status = models.CharField(max_length=20, default='Pending')

    # ✅ NEW
    handled_by = models.ForeignKey(
        Account,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='handled_emergencies'
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title