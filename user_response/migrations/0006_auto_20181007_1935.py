# Generated by Django 2.1.2 on 2018-10-07 19:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_response', '0005_auto_20181007_1933'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='User',
            new_name='UserDetails',
        ),
    ]
