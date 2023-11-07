from django.db import models

import Core.models


class News(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(Core.models.Account, on_delete=models.CASCADE)
    title = models.CharField(max_length=256)
    description = models.CharField(max_length=2500)
    date_of_publication = models.DateField()
    image = models.CharField(max_length=256)


class StarNews(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(Core.models.Account, on_delete=models.CASCADE)
    news = models.ForeignKey(News, on_delete=models.CASCADE)
    evaluation = models.IntegerField()
