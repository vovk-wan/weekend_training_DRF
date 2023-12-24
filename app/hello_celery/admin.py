import uuid

from django.contrib import admin
from hello_celery.models import TaskModel
from hello_celery.tasks.class_based_tasks import manual
from django.db import transaction


@admin.register(TaskModel)
class TaskAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        if not change:
            with transaction.atomic():
                task_id = uuid.uuid4()
                obj.task_id = task_id
                obj.save()
                transaction.on_commit(lambda: manual.apply_async(args=(obj.pk,), task_id=str(obj.task_id)))
