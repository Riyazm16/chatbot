# Generated by Django 2.1.2 on 2018-10-13 07:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_response', '0023_auto_20181013_0744'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='date',
            field=models.DateTimeField(default=None),
        ),
    ]
