# Generated by Django 2.2.7 on 2020-03-07 17:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('front', '0004_auto_20200307_0917'),
    ]

    operations = [
        migrations.CreateModel(
            name='hackersclub_donater',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('age1', models.IntegerField()),
                ('blood_group', models.TextField()),
                ('last_name', models.CharField(max_length=100)),
                ('phone_no', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='redcross_donater',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('age1', models.IntegerField()),
                ('blood_group', models.TextField()),
                ('last_name', models.CharField(max_length=100)),
                ('phone_no', models.IntegerField()),
            ],
        ),
    ]
