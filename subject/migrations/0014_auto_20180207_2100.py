# Generated by Django 2.0.1 on 2018-02-07 21:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('university', '0013_auto_20180207_2051'),
        ('subject', '0013_auto_20180205_1844'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subjectscore',
            name='univ_subject',
        ),
        migrations.AddField(
            model_name='subjectscorebycategory',
            name='univ_subject',
            field=models.ForeignKey(default=14, on_delete=django.db.models.deletion.CASCADE, related_name='scores_by_category', to='university.UniversitySubject'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='subjectscore',
            name='score_by_category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='scores', to='subject.SubjectScoreByCategory'),
        ),
    ]
