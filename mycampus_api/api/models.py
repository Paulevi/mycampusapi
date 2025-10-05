from django.db import models

# Create your models here.

class Actu(models.Model):
    id = models.AutoField(primary_key=True)
    titre = models.fields.CharField(max_length=100)
    contenu = models.fields.TextField()
    image = models.ImageField(upload_to='actu_images/', null=True, blank=True)
    date = models.fields.DateField()

    def __str__(self):
        return self.titre