# Generated by Django 2.2.4 on 2019-08-01 21:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('team', '0002_auto_20190801_1034'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='participant',
            field=models.ManyToManyField(related_name='_team_participant_+', to='team.Team'),
        ),
        migrations.DeleteModel(
            name='Participants',
        ),
    ]