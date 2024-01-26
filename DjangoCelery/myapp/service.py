from django.core.mail import send_mail


def send(user_email: str):
    send_mail(
        'Привет, это рассылка..',
        'Я тут посижу, а ты пока делай что хочешь',
        'djagnocelery@yandex.ru',
        [user_email],
        fail_silently=False
    )
