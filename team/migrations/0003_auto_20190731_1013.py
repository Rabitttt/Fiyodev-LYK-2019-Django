# Generated by Django 2.2.3 on 2019-07-31 07:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('team', '0002_team_owner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='event_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
