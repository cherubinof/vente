# Generated by Django 4.2.4 on 2023-08-12 17:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecomme', '0004_category_main_category_alter_slider_titre_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='slider',
            name='titre',
            field=models.CharField(choices=[('Bonne_affaire', 'Bonne_affaire'), ('Nouvelle_arrivage', 'Nouvelle_arrivage')], max_length=100),
        ),
    ]
