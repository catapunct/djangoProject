from django.db import models


class Trainer(models.Model):

    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    course = models.CharField(max_length=50)
    description = models.TextField(max_length=400)
    start_date = models.DateField()
    end_date = models.DateField()

    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


