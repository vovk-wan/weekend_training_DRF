"""
celery.py
---------
Модуль реализует представления для получения статуса задачи Целери
"""
from celery.result import AsyncResult
from drf_yasg.utils import swagger_auto_schema
from rest_framework import permissions, status, views
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response


class GetCeleryTaskState(views.APIView):
    """Класс реализует вью для получения статуса задачи целери"""

    permission_classes = (permissions.AllowAny,)

    def get(self, request, task_id):
        result = AsyncResult(task_id)
        result.result
        print(f'{result._get_task_meta()=}')
        try:
            if not hasattr(result, 'result'):
                raise ValidationError('Селери не вернул результат')
            response_data = result.result if result.result else dict(
                state=result.state,
                code='',
                detail='',
                meta=result.info)
            return Response(status=status.HTTP_200_OK, data=response_data)
        except ValidationError as e:
            return Response(
                status=status.HTTP_200_OK,
                data={'state': 'FAILURE', 'code': e.__class__.__name__, 'detail': 'Не удалось сериализовать ответ'},
            )
