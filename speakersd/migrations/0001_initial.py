# Generated by Django 4.0.5 on 2022-06-19 11:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Speaker',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('s_id', models.CharField(blank=True, max_length=5, null=True, unique=True)),
                ('name_of_speaker', models.CharField(max_length=400)),
                ('pic', models.FileField(blank=True, null=True, upload_to='')),
                ('address_citycountry', models.CharField(max_length=500)),
                ('phone_number', models.BigIntegerField(blank=True, null=True)),
                ('email_id', models.EmailField(max_length=254)),
                ('profession', models.CharField(max_length=500)),
                ('awards', models.TextField(blank=True)),
                ('desc', models.TextField()),
                ('books', models.TextField()),
                ('available_months', models.CharField(choices=[('NON', 'Unavailable'), ('JAN', 'January'), ('FEB', 'February'), ('MAR', 'March'), ('APR', 'April'), ('MAY', 'May'), ('JUN', 'June'), ('JUL', 'July'), ('AUG', 'August'), ('SEP', 'September'), ('OCT', 'October'), ('NOV', 'November'), ('DEC', 'December')], max_length=3)),
                ('upcoming_events', models.CharField(blank=True, max_length=400)),
                ('upload_date', models.DateField(auto_now=True, null=True)),
            ],
        ),
    ]
