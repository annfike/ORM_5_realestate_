# Generated by Django 2.2.24 on 2021-12-08 16:25

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0008_auto_20211208_1913'),
    ]

    operations = [
        migrations.CreateModel(
            name='Owner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('owner', models.CharField(db_index=True, max_length=200, verbose_name='ФИО владельца')),
                ('owners_phonenumber', models.CharField(db_index=True, max_length=20, verbose_name='Номер владельца')),
                ('owner_pure_phone', phonenumber_field.modelfields.PhoneNumberField(blank=True, db_index=True, max_length=128, null=True, region=None, verbose_name='Нормализованный номер владельца')),
                ('flat', models.ManyToManyField(db_index=True, related_name='flats', to='property.Flat', verbose_name='Квартиры в собственности')),
            ],
        ),
    ]