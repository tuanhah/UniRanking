# Generated by Django 2.0.3 on 2018-04-09 08:10

import score.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('university', '0005_auto_20180406_0257'),
    ]

    operations = [
        migrations.AlterField(
            model_name='universityscorebycriterion',
            name='score',
            field=models.FloatField(default=0, validators=[score.validators.ScoreValidator()]),
        ),
        migrations.AlterField(
            model_name='universityscorebycriterioncategory',
            name='score',
            field=models.FloatField(default=0, validators=[score.validators.ScoreValidator()]),
        ),
    ]
