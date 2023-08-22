# Generated by Django 4.2.4 on 2023-08-12 13:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pub',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rabais', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='media/pub_img')),
            ],
        ),
        migrations.CreateModel(
            name='Slider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titre', models.CharField(max_length=100)),
                ('texte', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='media/slider_img')),
            ],
        ),
    ]