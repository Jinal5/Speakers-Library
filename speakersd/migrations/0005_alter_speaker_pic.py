# Generated by Django 4.0.5 on 2022-06-19 19:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('speakersd', '0004_alter_speaker_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='speaker',
            name='pic',
            field=models.ImageField(blank=True, null=True, upload_to='images'),
        ),
    ]
