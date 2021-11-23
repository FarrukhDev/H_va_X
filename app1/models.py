from django.db import models
class Soz(models.Model):
    soz = models.CharField(max_length=20)
    def __str__(self):
        return self.soz

class N_soz(models.Model):
    n_soz = models.CharField(max_length=20)
    soz_id = models.ForeignKey(Soz, on_delete=models.CASCADE)
    def __str__(self):
        return self.n_soz

# Create your models here.
