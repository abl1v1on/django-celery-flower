from DjangoCelery.celery import app
from .models import Contact
from .service import send


@app.task
def send_spam_mail(user_mail: str):
    send(user_email=user_mail)
    

@app.task
def calc(a, b):
    Contact.objects.create(name='test', email='test@mail.ru')
    return a + b


# Таск будет пытаться что-то выполнить, но если словит ошибку, то повторит через 5 * 60 секунд

@app.task(bind=True, default_retry_delay=5 * 60)
def calc_retry(self, a, b):
    try:
        return a + b
    except Exception as ex:
        raise self.retry(exc=ex, coundown=60)

