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
    nb_ucd = models.FloatField()
    nb_doses = models.FloatField()

    def __str__(self):
        return (
            f"{self.code_region} - {self.libelle_region} - {self.code_departement} - "
            f"{self.libelle_departement} - {self.date_fin_semaine} - {self.type_de_vaccin} - "
            f"{self.nb_ucd} - {self.nb_doses}"
        )


class D_Date(models.Model):
    pk_date = models.DateField(primary_key=True)

    def __str__(self):
        return f"{self.pk_date}"


class D_Type(models.Model):
    pk_type = models.CharField(primary_key=True, max_length=30)

    def __str__(self):
        return f"{self.pk_type}"
