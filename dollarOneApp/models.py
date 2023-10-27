from django.db import models

# Create your models here.

class AccelorometerModel(models.Model):
    template_name = models.CharField(max_length=100)
    x = models.FloatField()
    y = models.FloatField()
    z = models.FloatField()
    longi = models.FloatField()
    lati = models.FloatField()

class GyroModel(models.Model):
    template_name = models.CharField(max_length=100)
    x = models.FloatField()
    y = models.FloatField()
    z= models.FloatField()
    longi = models.FloatField()
    lati = models.FloatField()

class MagnetModel(models.Model):
    template_name = models.CharField(max_length=100)
    x = models.FloatField()
    y = models.FloatField()
    z =models.FloatField()
    long=models.FloatField()
    lati=models.FloatField()
 
class classifiedTemplates(models.Model):
    template_name = models.CharField(max_length=100)
    distance = models.FloatField()
    alignment_Score= models.FloatField()
    long=models.FloatField()
    lati=models.FloatField()
    classified_by =models.CharField(
        max_length=50,
        choices=[
            ('Eucledian_Distance', 'Eucledian_Distance'),
            ('Alignment_similarity_score', 'Alignment_similarity_score')
        ]
    )
 
class identifyBehavior(models.Model):
    template_name = models.CharField(max_length=100)
    long=models.FloatField()
    lati=models.FloatField()
    behavior =models.CharField(
        max_length=10,
        choices=[
            ('Normal', 'Normal'),
            ('Abnormal', 'Abnormal')
        ]
    )