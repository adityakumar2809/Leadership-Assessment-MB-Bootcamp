# Generated by Django 3.0.8 on 2020-07-23 01:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mbTest', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='mbresponse',
            name='average_score',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='mbresponse',
            name='quadrant',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
