from django.db import models

# Create your models here.


class Music(models.Model):

    title = models.CharField(max_length=200)
    seconds = models.IntegerField()

    class Meta:
        db_table = 'music'
        verbose_name_plural = 'Musícas'

    def __str__(self):
        return self.title