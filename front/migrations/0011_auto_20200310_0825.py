# Generated by Django 2.2.7 on 2020-03-10 16:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('front', '0010_auto_20200310_0822'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bloodmanagement',
            name='phone_no',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='cust',
            name='phone_no',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='hackersclub_donater',
            name='phone_no',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='redcross_donater',
            name='phone_no',
            field=models.CharField(max_length=50),
        ),
    ]