# Generated by Django 2.0.1 on 2018-03-18 02:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('subject', '0021_auto_20180317_0855'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='GroupSubject',
            new_name='SubjectGroup',
        ),
        migrations.AlterModelTable(
            name='subjectgroup',
            table='subject_group',
        ),
    ]