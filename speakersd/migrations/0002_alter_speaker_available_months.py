# Generated by Django 4.0.5 on 2022-06-19 14:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('speakersd', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='speaker',
            name='available_months',
            field=models.CharField(choices=[('NON', 'Unavailable'), ('JAN', 'January'), ('FEB', 'February'), ('MAR', 'March'), ('APR', 'April'), ('MAY', 'May'), ('JUN', 'June'), ('JUL', 'July'), ('AUG', 'August'), ('SEP', 'September'), ('OCT', 'October'), ('NOV', 'November'), ('DEC', 'December')], max_length=3, null=True),
        ),
    ]
