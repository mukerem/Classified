# Generated by Django 3.0.4 on 2021-05-09 12:31

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('region', models.CharField(choices=[('Addis Ababa', 'Addis Ababa'), ('Afar', 'Afar'), ('Amhara', 'Amhara'), ('Benishangul-Gumuz', 'Benishangul-Gumuz'), ('Dire Dawa', 'Dire Dawa'), ('Gambela', 'Gambela'), ('Harari', 'Harari'), ('Oromia', 'Oromia'), ('Sidama', 'Sidama'), ('Somali', 'Somali'), ("Southern Nations, Nationalities, and Peoples' Region", "Southern Nations, Nationalities, and Peoples' Region"), ('Tigray', 'Tigray')], max_length=100)),
                ('city', models.CharField(max_length=1000)),
                ('specific_location', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Seller',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=15, validators=[django.core.validators.RegexValidator(message='Phone number must be entered in the format : 09******** or +2519******** up to 15 digits allowed', regex='^\\+?1?\\d{10,15}$')])),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Seller.Location')),
            ],
        ),
    ]