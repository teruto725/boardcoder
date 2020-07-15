from django.db import models

# Create your models here.
from accounts.models import CustomUser


class Room(models.Model):
    name = models.CharField(max_length=200, unique=True)
    gamename = models.CharField(max_length=10)
    password = models.CharField(max_length=20)
    user1 = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="user1", null=True, blank=True)
    user2 = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="user2", null=True, blank=True)
    user3 = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="user3", null=True, blank=True)
    user4 = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="user4", null=True, blank=True)

    def add_user(self, user):
        users = self.get_user_list()
        for i in range(len(users)):
            if users[i] is None:
                self.set_user(user, i)
                print(user)
                print(self.user1)
                self.save()# dont forget!
                return "success"
            elif users[i].pk == user.pk:
                return "already"
        else:
            return "full"

    def disconnect(self, user):
        users = self.get_user_list()
        for i in range(len(users)) :
            if users[i].pk == user.pk:
                self.set_user(None, i)
                self.save()
                return "success"
        return "no_exist"

    def get_user_list(self):
        li = [self.user1, self.user2, self.user3, self.user4]
        return li

    def set_user(self, user, idx):
        if idx == 0:
            self.user1 = user
        elif idx == 1:
            self.user2 = user
        elif idx == 2:
            self.user3 = user
        elif idx == 3:
            self.user4 = user
