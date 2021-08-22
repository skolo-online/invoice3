from django.core.mail import EmailMessage
from django.conf import settings



def emailInvoiceClient(to_email, from_client, filepath):
    from_email = settings.EMAIL_HOST_USER
    subject = '[Skolo] Invoice Notification'
    body = """
    Good day,

    Please find attached invoice from {} for your immediate attention.

    regards,
    Skolo Online Learning
    """.format(from_client)

    message = EmailMessage(subject, body, from_email, [to_email])
    message.attach_file(filepath)
    message.send()
