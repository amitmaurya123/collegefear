# Generated by Django 3.0.3 on 2020-05-04 15:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basic_app', '0011_auto_20200504_1934'),
    ]

    operations = [
        migrations.AddField(
            model_name='exam',
            name='subject',
            field=models.CharField(default='All', max_length=15),
        ),
        migrations.AlterField(
            model_name='exam',
            name='college',
            field=models.CharField(choices=[('NIT KURUKSHETRA', 'NIT KURUKSHETRA'), ('NIT ALLAHABAD', 'NIT ALLAHABAD'), ('NIT PATNA', 'NIT PATNA'), ('NIT JAMSHEDPUR', 'NIT JAMSHEDPUR'), ('NIT CALICUT', 'NIT CALICUT'), ('NIT SURATHKAL', 'NIT SURATHKAL')], default='NIT KURUKSHETRA', max_length=200),
        ),
    ]