from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags

def send_email(subject, template, context, recipient_list):
    html_message = render_to_string(template, context)
    plain_message = strip_tags(html_message)
    send_mail(subject, plain_message, 'from@example.com', recipient_list, html_message=html_message)

def send_registration_confirmation_email(user):
    subject = 'Подтверждение регистрации'
    template = 'emails/registration_confirmation.html'
    context = {'user': user}
    recipient_list = [user.email]
    send_email(subject, template, context, recipient_list)

def send_response_notification_email(response):
    subject = 'Новый отклик на ваше объявление'
    template = 'emails/response_notification.html'
    context = {'response': response}
    recipient_list = [response.ad.user.email]
    send_email(subject, template, context, recipient_list)