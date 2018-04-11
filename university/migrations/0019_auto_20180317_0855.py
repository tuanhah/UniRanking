# Generated by Django 2.0.1 on 2018-03-17 08:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('university', '0018_auto_20180315_1831'),
    ]

    operations = [
        migrations.RenameField(
            model_name='university',
            old_name='ranking_position',
            new_name='rank',
        ),
        migrations.AddField(
            model_name='university',
            name='overall_score',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='universityscore',
            name='score_by_category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cri_scores', to='university.UniversityScoreByCategory'),
        ),
    ]