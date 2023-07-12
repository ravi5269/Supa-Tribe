from django.db import models
from twilio.rest import Client

# Create your models here.


class Score(models.Model):
    result = models.PositiveIntegerField()

    def __str__(self):
        return str(self.result)

    def save(self, *args, **kwargs):
        # if self.result < 100:
        account_sid = "AC9481d0154f00421ecd501e36d5910001"
        auth_token = "fb49313eb16e2d9639b3d8ab1e99f621"
        client = Client(account_sid, auth_token)
        message = client.messages.create(
            body="+917869144369", from_="+12345163703", to="+917869144369"
        )

        print(message.sid)
        return super().save()
