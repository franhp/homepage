# Generated by Django 2.0.2 on 2018-03-04 16:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tvseries', '0007_auto_20180304_1624'),
    ]

    operations = [
        migrations.AlterField(
            model_name='title',
            name='title_type',
            field=models.CharField(choices=[('movie', 'Movie'), ('tvSeries', 'TV Series'), ('short', 'Short')], max_length=20),
        ),
    ]