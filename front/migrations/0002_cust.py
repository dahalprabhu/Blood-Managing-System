# Generated by Django 2.2.7 on 2020-02-12 02:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('front', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='cust',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('age1', models.IntegerField()),
                ('blood_group', models.TextField()),
                ('last_name', models.CharField(max_length=100)),
            ],
        ),
    ]
