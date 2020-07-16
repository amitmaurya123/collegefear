# Generated by Django 3.0.3 on 2020-05-10 07:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basic_app', '0018_userprofileinfo'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofileinfo',
            name='year',
            field=models.CharField(choices=[('1st', '1st'), ('2nd', '2nd'), ('3rd', '3rd'), ('4th', '4th')], default='2nd', max_length=10),
        ),
    ]