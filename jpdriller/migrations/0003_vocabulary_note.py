# Generated by Django 2.0.4 on 2018-05-04 15:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jpdriller', '0002_katakana_vocabulary'),
    ]

    operations = [
        migrations.AddField(
            model_name='vocabulary',
            name='note',
            field=models.CharField(max_length=20, null=True, verbose_name='Note'),
        ),
    ]
