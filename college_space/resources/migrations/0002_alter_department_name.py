# Generated by Django 3.2.6 on 2021-10-07 05:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resources', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='department',
            name='name',
            field=models.CharField(max_length=50, primary_key=True, serialize=False),
        ),
    ]
