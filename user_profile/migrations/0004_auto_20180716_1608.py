# Generated by Django 2.0.6 on 2018-07-16 16:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0003_auto_20180617_1531'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='birthday',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='description',
            field=models.TextField(blank=True, max_length=250),
        ),
        migrations.AlterField(
            model_name='profile',
            name='education',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
