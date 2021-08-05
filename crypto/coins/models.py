from django.db import models

# Create your models here.
class Coin(models.Model):
    name = models.CharField(max_length=10)
    symbol = models.CharField(max_length=50)
    price = models.FloatField(default=0,blank=True)
    image=models.URLField(blank=True,null=True)
    rank = models.IntegerField(default=0,blank=True)
    market_cap=models.BigIntegerField(default=0,blank=True)

    def __str__(self):
        return str(self.name)

    class Meta:
        ordering = ['rank']