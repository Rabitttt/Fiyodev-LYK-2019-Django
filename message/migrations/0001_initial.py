# Generated by Django 2.2.3 on 2019-08-01 07:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField(max_length=280)),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
