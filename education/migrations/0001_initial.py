# Generated by Django 2.1.7 on 2019-03-28 13:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0009_alter_user_last_name_max_length'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Log',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=1280, null=True)),
                ('creationDate', models.DateTimeField(auto_now_add=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120, null=True)),
                ('url', models.CharField(blank=True, max_length=120, null=True)),
                ('is_parent', models.BooleanField(default=True)),
                ('is_show', models.BooleanField(default=True)),
                ('fa_icon', models.CharField(blank=True, max_length=120, null=True)),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='education.Menu')),
                ('permission', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='auth.Permission')),
            ],
        ),
        migrations.CreateModel(
            name='Parent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profileImage', models.ImageField(blank=True, null=True, upload_to='profile/', verbose_name='Profil Resmi')),
                ('address', models.TextField(blank=True, null=True, verbose_name='Adres')),
                ('mobilePhone', models.CharField(max_length=120, verbose_name='Telefon Numarası')),
                ('gender', models.CharField(choices=[('Erkek', 'Erkek'), ('Kadın', 'Kadın')], default='Erkek', max_length=128, verbose_name='Cinsiyeti')),
                ('tc', models.CharField(blank=True, max_length=128, null=True, verbose_name='T.C. Kimlik Numarası')),
                ('birthDate', models.DateField(null=True, verbose_name='Doğum Tarihi')),
                ('creationDate', models.DateTimeField(auto_now_add=True, verbose_name='Kayıt Tarihi')),
                ('modificationDate', models.DateTimeField(auto_now=True, verbose_name='Güncelleme Tarihi')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profileImage', models.ImageField(blank=True, null=True, upload_to='profile/', verbose_name='Profil Resmi')),
                ('address', models.TextField(blank=True, null=True, verbose_name='Adres')),
                ('mobilePhone', models.CharField(max_length=120, verbose_name='Telefon Numarası')),
                ('studentNumber', models.CharField(max_length=128, verbose_name='Öğrenci Numarası')),
                ('gender', models.CharField(choices=[('Erkek', 'Erkek'), ('Kadın', 'Kadın')], default='Erkek', max_length=128, verbose_name='Cinsiyeti')),
                ('tc', models.CharField(blank=True, max_length=128, null=True, verbose_name='T.C. Kimlik Numarası')),
                ('birthDate', models.DateField(null=True, verbose_name='Doğum Tarihi')),
                ('creationDate', models.DateTimeField(auto_now_add=True, verbose_name='Kayıt Tarihi')),
                ('modificationDate', models.DateTimeField(auto_now=True, verbose_name='Güncelleme Tarihi')),
                ('parents', models.ManyToManyField(to='education.Parent')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'permissions': (('student_add', 'Öğrenci Ekle'), ('student_list', 'Öğrenci Liste'), ('update_student', 'Öğrenci Güncelle')),
            },
        ),
    ]
