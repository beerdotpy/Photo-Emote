# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('image_id', models.CharField(max_length=10, editable=False)),
                ('url', models.ImageField(upload_to=b'static/images')),
                ('created_at', models.DateTimeField(editable=False)),
                ('description', models.TextField()),
                ('orientation', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('like_type', models.CharField(default=b'Like', max_length=20)),
                ('pixels', models.CharField(max_length=50)),
                ('image_id', models.ForeignKey(to='photoEmote.Image')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('device_id', models.CharField(max_length=255)),
                ('user_id', models.CharField(max_length=10, editable=False)),
            ],
        ),
        migrations.AddField(
            model_name='like',
            name='user_id',
            field=models.ForeignKey(to='photoEmote.User'),
        ),
        migrations.AddField(
            model_name='image',
            name='user_id',
            field=models.ForeignKey(to='photoEmote.User'),
        ),
    ]
