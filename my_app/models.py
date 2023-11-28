from django.db import models

class GYM(models.Model):
    name = models.CharField(max_length=255,verbose_name="adi")
    adress = models.TextField(verbose_name='adress')

    def __str__(self):
        return self.name

    class Meta:
        ordering = ("name", )
        verbose_name = "ad"
        verbose_name_plural = "adlari"



class Trainer(models.Model):
   
    name = models.CharField(max_length=255, verbose_name="adi")
    specialization = models.CharField(max_length=255, verbose_name="peshesi")
    gym = models.OneToOneField(GYM, on_delete=models.SET_NULL, null=True, blank=True)
   
    def __str__(self):
        return self.name

    class Meta:
        ordering = ("name",)
        verbose_name = "mesqci"
        verbose_name_plural = "mesqciler"

class Client(models.Model):
   
    name = models.CharField(max_length=255, verbose_name="adi")
    age = models.IntegerField(verbose_name='yashi')
   
    def __str__(self):
        return self.name

    class Meta:
        ordering = ("name",)
        verbose_name = "musteri"
        verbose_name_plural = "musteriler"


class WorkoutSession(models.Model):

    client = models.ForeignKey(Client, on_delete=models.SET_NULL, null=True, blank=True)
    trainer = models.ForeignKey(Trainer, on_delete=models.SET_NULL, null=True, blank=True )
    date = models.DateField(verbose_name='tarix')
    duration = models.IntegerField(verbose_name='say')

    def __str__(self):
        return self.client

    class Meta:
        ordering = ("client",)
        verbose_name = "mesq vaxti"
        verbose_name_plural = "mesq vaxtlari"



