import celery
from market.celery import app
from celery.utils.log import get_task_logger
from celery.exceptions import SoftTimeLimitExceeded


class BaseTask(celery.Task):
    ignore_result = False
    track_started = True
    default_retry_delay = 5
    max_retries = 3
    autoretry_for = (IndexError, ValueError)
    dont_autoretry_for = (ConnectionError,)
    time_limit = 100
    soft_time_limit = 80

    def __init__(self):
        super(BaseTask, self).__init__()
        self.logger = get_task_logger(self.__class__.__name__)

    def on_failure(self, exc, task_id, args, kwargs, einfo):
        self.logger.warning(f'Событие: фиаско: {task_id=}')
        self.logger.warning(f'{args=}')
        self.logger.warning(f'{kwargs=}')
        self.logger.warning(f'{einfo=}')
        self.logger.error(exc)

    def on_retry(self, exc, task_id, args, kwargs, einfo):
        self.logger.warning(f'Событие: повтор запуска: {task_id=}')

    def on_success(self, retval, task_id, args, kwargs):
        self.logger.warning(f'событие: успех: {task_id=}')

    def on_timeout(self, soft, timeout):
        super(BaseTask, self).on_timeout(soft, timeout)
        self.update_state(state='SOFT_TIME_LIMIT', meta={'percent': -1})


@app.task(base=BaseTask)
def fail_task_with_value_error():
    raise ValueError('Здесь нельзя называть это имя')


@app.task
def fail_task_with_index_error():
    raise IndexError('корявый индекс')


@app.task
def error_handler(request, exc, traceback):
    print(f'{request.id=}')
    print(f'{exc=}')
    print('пример обработки ошибки через связывание')


@app.task(base=BaseTask)
def fail_base_task_with_index_error():
    raise IndexError('корявый индекс у базовой задачи')


@app.task(base=BaseTask, bind=True)
def manual(self, obj_id):
    from hello_celery.models import TaskModel
    import time
    obj = TaskModel.objects.get(pk=obj_id)
    for i in range(50):
        self.update_state(state='PROGRESS', meta={'percent': i * 100 / 50})
        self.logger.info(f'progress: {i}')
        time.sleep(2)
    self.logger.warning(f'{obj=}')


if __name__ == '__main__':
    fail_task_with_index_error.apply_async(link_error=error_handler.s())
    fail_base_task_with_index_error.apply_async(link_error=error_handler.s())
