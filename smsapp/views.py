from django.shortcuts import render
from django.core.mail import send_mail

# Create your views here.
def home (request):
    send_mail(
        "testing mail",
        "Here is the message.",
        "holkar.msc@gmail.com",
        ["ravipatelkant@gmail.com"],
        fail_silently=False,
    )