from django.db import models
class Plante(models.Model):
    nom = models.CharField(max_length=100)
    type_plante = models.CharField(max_length=50)
    date_plantation = models.DateField()
    arrosage_frequence = models.CharField(max_length=50)
    description = models.TextField()

    def __str__(self):
        return self.nom
# Create your models here.
