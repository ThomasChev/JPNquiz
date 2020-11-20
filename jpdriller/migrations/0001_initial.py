# Generated by Django 2.0.4 on 2018-05-03 15:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Hiragana',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False, verbose_name='Identifier')),
                ('hiragana', models.CharField(max_length=6, verbose_name='Hiragana')),
                ('romanji', models.CharField(max_length=6, verbose_name='Romanji')),
            ],
        ),
    ]
