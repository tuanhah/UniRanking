# Generated by Django 2.0.1 on 2018-02-05 16:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('university', '0009_universityscore_score_by_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='universityscore',
            name='score_by_category',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='university.UniversityScoreByCategory'),
        ),
    ]
