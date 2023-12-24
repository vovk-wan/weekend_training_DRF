from django.db import models
import uuid
# Create your models here.


class TaskModel(models.Model):
    task_id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    log = models.TextField()
    state = models.CharField(max_length=100)