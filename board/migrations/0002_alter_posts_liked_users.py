# Generated by Django 3.2 on 2021-08-07 15:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posts',
            name='liked_users',
            field=models.TextField(blank=True, default='None,', null=True),
        ),
    ]
