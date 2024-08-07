from django.db import models

# Create your models here.

class Urunler(models.Model):
    urunismi=models.CharField(max_length=100,verbose_name="Ürün İsmi")
    aciklama=models.TextField(max_length=100,verbose_name="Açıklama")
    fiyat=models.IntegerField(default=0,verbose_name="Fiyat")
    resim=models.FileField(upload_to='urunResmi',null=True,blank=True)#burada az önce settingsde belirttiğimiz upload klasörünü oluşturup altına bu urun resmi kalsörünü oluşturacak ardından nullardan biri boş olabilir diğeri
    #boş bırakılabilir demek.

    def __str__(self):
        return self.urunismi  #ürün ismini yazar admin kısmında
