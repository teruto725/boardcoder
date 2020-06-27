from django.db import models
from accounts.models import CustomUser

GAME_OPTIONS = (("ja","じゃんけん"),("gomoku","五目並べ"))




"""
class Room(models.Model):
    question_text = models.CharField(max_length=200)
    gameid = models.IntegerField(default=0)
    user1 = models.ForeignKey(Agent,on_delete=models.CASCADE)
"""


