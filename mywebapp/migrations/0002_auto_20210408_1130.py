# Generated by Django 3.1.7 on 2021-04-08 06:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mywebapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projects',
            name='description',
            field=models.TextField(default='Description here'),
        ),
        migrations.AlterField(
            model_name='projects',
            name='github_url',
            field=models.URLField(blank=True, default='https://www.addlinkhere.com'),
        ),
        migrations.AlterField(
            model_name='projects',
            name='title',
            field=models.CharField(default='Title here', max_length=200),
        ),
    ]