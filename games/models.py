from django.db import models
from accounts.models import CustomUser

GAME_OPTIONS = (("ja","じゃんけん"),("gomoku","五目並べ"))


class Room(models.Model):
    question_text = models.CharField(max_length=200)
    game = models.CharField(max_length=10)
    user1 = models.ForeignKey(CustomUser,)
    user1 = models.ForeignKey(CustomUser,on_delete=models.CASCADE)




