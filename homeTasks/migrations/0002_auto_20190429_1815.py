# Generated by Django 2.1.4 on 2019-04-29 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homeTasks', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article1',
            name='post',
            field=models.TextField(blank=True, default=''),
        ),
    ]
