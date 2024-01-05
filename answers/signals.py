# from django.db.models.signals import post_save
# from django.dispatch import receiver
# from .models import Answer
# from django.template.loader import render_to_string
# from django.core.mail import send_mail
# from django.core import mail
# from django.core.mail import EmailMessage

# @receiver(post_save, sender=Answer)
# def after_answer_save(sender, instance, **kwargs):
#     subject = 'Answered to question'
#     recipient_email = instance.question.user.email
#     html_content = render_to_string('answers/email_answer.html', {'answer': instance})

#     email = EmailMessage(
#         subject,
#         html_content,
#         'nouman.ali@devsinc.com',
#         [recipient_email],
#     )
#     email.content_subtype = "html"  # Set the content type to HTML
#     email.send()

#     post_save.connect(after_answer_save, sender=Answer)
