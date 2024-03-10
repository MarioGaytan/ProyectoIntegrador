# Generated by Django 5.0.3 on 2024-03-10 01:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_usuario', models.IntegerField()),
                ('usuario', models.CharField(max_length=255)),
                ('fecha_publicacion', models.DateField()),
                ('contenido', models.TextField()),
                ('Imagen', models.ImageField(blank=True, null=True, upload_to='uploads/')),
            ],
        ),
    ]
