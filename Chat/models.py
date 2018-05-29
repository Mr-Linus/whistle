from django.db import models
from User.models import User
# Create your models here.


class Chat(models.Model):
    sender = models.ForeignKey(User,verbose_name='has_chats', on_delete=models.CASCADE)
    content = models.TextField(max_length=200)
    time = models.DateTimeField(auto_now_add=True, null=True)
    def __unicode__(self):
        return self.content
