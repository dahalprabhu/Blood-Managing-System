# Generated by Django 2.2.7 on 2020-03-07 23:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('front', '0008_auto_20200307_1513'),
    ]

    operations = [
        migrations.AddField(
            model_name='bloodmanagement',
            name='address',
            field=models.CharField(default=0, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cust',
            name='address',
            field=models.CharField(default=0, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='hackersclub_donater',
            name='address',
            field=models.CharField(default=0, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='redcross_donater',
            name='address',
            field=models.CharField(default=0, max_length=100),
            preserve_default=False,
        ),
    ]