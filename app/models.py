from django.db import models


# Create your models here.
class ODS(models.Model):
    """ODS

    """
    code_region = models.CharField(max_length=10)
    libelle_region = models.CharField(max_length=255)
    code_departement = models.CharField(max_length=10)
    libelle_departement = models.CharField(max_length=255)
    date_fin_semaine = models.DateField()
    type_de_vaccin = models.CharField(max_length=100)
    nb_ucd = models.IntegerField()
    nb_doses = models.IntegerField()

    def __str__(self):
        return (
            f"{self.code_region} - {self.libelle_region} - {self.code_departement} - "
            f"{self.libelle_departement} - {self.date_fin_semaine} - {self.type_de_vaccin} - "
            f"{self.nb_ucd} - {self.nb_doses}"
        )
