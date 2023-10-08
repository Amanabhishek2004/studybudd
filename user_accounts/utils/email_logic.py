from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings
from user_accounts.models import *


def verify_email(email, token):
    page = "verify"
      # Assuming you have a logged-in user
    # purchase = Product.objects.filter().order_by("-created").first()
    subject = "VERIFY YOUR EMAIL"
    message = f"click on the link to verify email http://127.0.0.1:8000/{token}"

    recipient_list = [email]  # Replace with the recipient's email address

    send_mail(subject, settings.EMAIL_HOST_USER,
              recipient_list, message=message)

    # Add any other logic or response here


def send_invoice_email(user,request):
    
    purchased_item = Customer.objects.filter(
        name=user).order_by("-created").first()
    value = purchased_item.Product_purchased.name
    subject = f"INVOICE FOR THE PURCHASE OF {value}"
    html_message = render_to_string(
        'email_template.html', {'user': user, "item": purchased_item})
    recipient_list = [user.email]  # Replace with the recipient's email address
    send_mail(subject, settings.EMAIL_HOST_USER,
              recipient_list, html_message=html_message)


