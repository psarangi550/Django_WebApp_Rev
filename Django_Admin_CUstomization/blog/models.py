from django.db import models

# Create your models here.


class Equipment(models.Model):
    cp_number=models.CharField(max_length=100)
    sne_id=models.IntegerField()

    def __str__(self):
        return self.cp_number

    class Meta:
        verbose_name='Equipments'
