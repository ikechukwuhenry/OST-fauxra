from django.db import models

class Question(models.Model):
    text = models.CharField(max_length=1000)
    date = models.DateTimeField('date published')

    def __str__(self):
        return self.text

class Answer(models.Model):
    question = models.ForeignKey(Question)
    text = models.CharField(max_length=1000)
    date = models.DateTimeField('date published')

    def __str__(self):
        return self.text
