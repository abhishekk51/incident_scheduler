
from django.db import models


class Incidents(models.Model):

    type = models.CharField(max_length=255)
    severity = models.IntegerField(choices=[(i, str(i)) for i in range(1, 5)], db_index=True)
    timestamp = models.DateTimeField(auto_now_add=True, db_index=True)
    description = models.TextField(null=True, blank=True)
    status = models.CharField(max_length=255, default="pending", choices=[("pending", "Pending"), ("assigned", "Assigned"), ("resolved", "resolved"), ("escalated", "Escalated")])
    assigned_to = models.ForeignKey('Handler', on_delete=models.DO_NOTHING, null=True, blank=True)


class Handler(models.Model):
    name = models.CharField(max_length=255)

