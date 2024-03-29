# Generated by Django 2.2.3 on 2019-08-01 07:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Participants',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('team_date', models.DateTimeField(auto_now=True)),
                ('event_type', models.CharField(choices=[('CTF', 'CTF'), ('Hackathon', 'Hackathon'), ('Meetup', 'Meetup'), ('Real Project', 'Real Project'), ('Other', 'Other')], max_length=50)),
                ('event_name', models.CharField(max_length=30)),
                ('event_information', models.TextField(max_length=500)),
                ('event_date', models.DateTimeField(blank=True, null=True)),
            ],
        ),
    ]
