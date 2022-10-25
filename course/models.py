from django.db import models

from trainer.models import Trainer


class Training(models.Model):

    name = models.CharField(max_length=30)
    trainer = models.ForeignKey(Trainer, on_delete=models.CASCADE)

    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name