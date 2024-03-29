# Generated by Django 2.2.4 on 2019-08-01 20:22

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20190801_1609'),
    ]

    operations = [
        migrations.RenameField(
            model_name='usertable',
            old_name='social_media',
            new_name='gitlab_link',
        ),
        migrations.AlterField(
            model_name='usertable',
            name='likes',
            field=models.ManyToManyField(related_name='liked_by', to=settings.AUTH_USER_MODEL),
        ),
    ]
