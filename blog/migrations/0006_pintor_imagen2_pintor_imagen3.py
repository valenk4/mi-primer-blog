# Generated by Django 5.2.3 on 2025-06-23 06:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_pintor_imagen_pintor_informacion_adicional'),
    ]

    operations = [
        migrations.AddField(
            model_name='pintor',
            name='imagen2',
            field=models.ImageField(blank=True, null=True, upload_to='artistas/'),
        ),
        migrations.AddField(
            model_name='pintor',
            name='imagen3',
            field=models.ImageField(blank=True, null=True, upload_to='artistas/'),
        ),
    ]
