# Generated by Django 2.2.4 on 2019-08-01 13:09

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20190801_1607'),
    ]

    operations = [
        migrations.AddField(
            model_name='usertable',
            name='likes',
            field=models.ManyToManyField(related_name='_usertable_likes_+', to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='Like',
        ),
    ]
