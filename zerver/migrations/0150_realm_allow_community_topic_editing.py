# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-28 22:56
from __future__ import unicode_literals

from django.db import migrations, models
from django.db.backends.postgresql_psycopg2.schema import DatabaseSchemaEditor
from django.db.migrations.state import StateApps


class Migration(migrations.Migration):

    dependencies = [
        ('zerver', '0149_realm_emoji_drop_unique_constraint'),
    ]

    operations = [
        migrations.AddField(
            model_name='realm',
            name='allow_community_topic_editing',
            field=models.BooleanField(default=False),
        ),
    ]