from market.celery import app
from celery.utils.log import get_task_logger


logger = get_task_logger('ping.logger')


@app.task
def ping():
    logger.info('pong')


@app.task(bind=True)
def echo(self, input: str):
    logger.info(f'echo: {input}')


@app.task(
    bind=True,
    max_retries=3,
    default_retry_delay=2,
    autoretry_for=(IndexError, ValueError)
)
def fail_echo(self, input: str):
    index = self.request.retries
    logger.info(f'echo {index + 1}: {input}')
    if index < 3:
        raise IndexError()
    raise ConnectionError('соединение не соединение')