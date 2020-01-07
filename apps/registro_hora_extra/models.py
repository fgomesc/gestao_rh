from django.db import models

class RegistroHoraExtra(models.Model):
    motivo = models.CharField(max_length=1000)

    def __str__(self):
        return self.motivo