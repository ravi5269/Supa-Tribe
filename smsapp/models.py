from django.db import models
from  twilio.rest import Client
# Create your models here.

class Score(models.Model):
    result = models.PositiveIntegerField()

    def __str__(self):
        return str(self.result)
    
    def save(self,*args, **kwargs):
        if self.result < 100:
            account_sid = 'AC73f4003c8dda735c9ba5157f4cc008ae'
            auth_token =   '397e4e30fe2e39384c9599bcb1efde1e'
            client = Client(account_sid, auth_token)

            message = client.messages.create(
                                        body=f'The current result is bad - {self.result}',
                                        from_='+16183504501',
                                        to='+917869144369',
                                    )

            print(message.sid)
        return super().save()(*args, **kwargs)
