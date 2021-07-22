# Generated by Django 3.0.5 on 2020-04-29 13:02

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('candidates', '0002_candidate_ccjrequestmade'),
    ]

    operations = [
        migrations.AddField(
            model_name='candidate',
            name='dbsrequestmade',
            field=models.DateTimeField(db_column='dbsrequestmade', default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='candidate',
            name='enhanceddbsrequestmade',
            field=models.DateTimeField(db_column='enhanceddbsrequestmade', default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='candidate',
            name='righttoworkrequestmade',
            field=models.DateTimeField(db_column='righttoworkrequestmade', default=django.utils.timezone.now),
        ),
    ]
