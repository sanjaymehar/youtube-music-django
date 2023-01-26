# Generated by Django 3.2.10 on 2022-01-05 07:43

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('release', models.DateField(default=datetime.datetime(2022, 1, 5, 13, 13, 21, 895935))),
                ('genre', models.CharField(max_length=100)),
                ('image', models.FileField(upload_to='')),
                ('uid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('genre', models.CharField(max_length=100)),
                ('lyricists', models.CharField(max_length=100)),
                ('file', models.FileField(upload_to='')),
                ('alid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dhun.album')),
            ],
        ),
    ]