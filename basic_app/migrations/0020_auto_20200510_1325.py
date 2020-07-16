# Generated by Django 3.0.3 on 2020-05-10 07:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basic_app', '0019_userprofileinfo_year'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofileinfo',
            name='year',
        ),
        migrations.AddField(
            model_name='userprofileinfo',
            name='semester',
            field=models.PositiveIntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8)], default=4),
        ),
    ]