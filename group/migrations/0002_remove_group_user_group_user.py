# Generated by Django 4.1.7 on 2023-03-12 20:15

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('group', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='group',
            name='user',
        ),
        migrations.AddField(
            model_name='group',
            name='user',
            field=models.ManyToManyField(null=True, to=settings.AUTH_USER_MODEL),
        ),
    ]