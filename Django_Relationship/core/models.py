from django.db import models


# Create your models here.
class Equipment(models.Model):
    cp_number = models.CharField(max_length=100)
    sne_id = models.IntegerField()
    trs_area = models.CharField(max_length=100)

    def __str__(self):
        return self.cp_number


class PACSData(models.Model):
    equipment=models.ForeignKey(Equipment,on_delete=models.CASCADE)
    scheme_number=models.IntegerField()
    model_type = models.CharField(max_length=100)

    def __str__(self):
        return self.model_type

