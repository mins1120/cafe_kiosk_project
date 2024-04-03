from django.db import models

class Question(models.Model):
    drink_type = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.drink_type

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    detailed_drink_type = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.detailed_drink_type} - Votes: {self.votes}"
