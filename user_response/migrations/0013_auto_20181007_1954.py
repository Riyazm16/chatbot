# Generated by Django 2.1.2 on 2018-10-07 19:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_response', '0012_auto_20181007_1953'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.DeleteModel(
            name='Person',
        ),
        migrations.DeleteModel(
            name='Userz',
        ),
    ]