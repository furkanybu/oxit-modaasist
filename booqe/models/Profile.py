from django.contrib.auth.models import User
from django.db import models


class Profile(models.Model):
    MALE = 'Erkek'
    FEMALE = 'Kadın'
    UNKNOWN = 'Belirtmek İstemiyorum'

    GENDER_CHOICES = (
        (MALE, 'Erkek'),
        (FEMALE, 'Kadın'),
        (UNKNOWN,'Belirtmek İstemiyorum')
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profileImage = models.ImageField(upload_to='profile/', null=True, blank=True, verbose_name='Profil Resmi')
    mobilePhone = models.CharField(max_length=120, verbose_name='Telefon Numarası', null=True, blank=True)
    gender = models.CharField(max_length=128, verbose_name='Cinsiyeti', choices=GENDER_CHOICES, default=MALE)
    birthDate = models.DateField(null=True, verbose_name='Doğum Tarihi')
    creationDate = models.DateTimeField(auto_now_add=True, verbose_name='Kayıt Tarihi')
    modificationDate = models.DateTimeField(auto_now=True, verbose_name='Güncelleme Tarihi')
    imei = models.CharField(max_length=200, verbose_name='IMEI', null=True, blank=True)
    gcm_registerID = models.CharField(max_length=512, verbose_name='token', null=True, blank=True)
    birth_year = models.IntegerField(verbose_name='Doğum Yılı', blank=True, null=True)
    city = models.CharField(max_length=255, verbose_name="Şehir", blank=True, null=True)
    notification = models.BooleanField(default=True)
