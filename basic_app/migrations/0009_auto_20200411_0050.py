# Generated by Django 3.0.3 on 2020-04-10 19:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basic_app', '0008_auto_20200409_2247'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exam',
            name='branch',
            field=models.CharField(choices=[('CS', 'CS'), ('ME', 'ME'), ('PIE', 'PIE'), ('EE', 'EE'), ('CE', 'CE'), ('ECE', 'ECE'), ('IT', 'IT')], max_length=200),
        ),
    ]
