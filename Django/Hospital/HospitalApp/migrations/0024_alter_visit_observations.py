# Generated by Django 5.0.4 on 2024-05-03 21:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HospitalApp', '0023_alter_visit_observations'),
    ]

    operations = [
        migrations.AlterField(
            model_name='visit',
            name='observations',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
