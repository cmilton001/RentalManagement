# Generated by Django 3.2.4 on 2021-06-30 03:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rentalsite', '0004_auto_20210629_1425'),
    ]

    operations = [
        migrations.AddField(
            model_name='annualrentallist',
            name='summaryordetail',
            field=models.CharField(default='S', max_length=1),
        ),
        migrations.AddField(
            model_name='buyoutcandidates',
            name='todaterentals',
            field=models.CharField(default='', max_length=200),
        ),
    ]
