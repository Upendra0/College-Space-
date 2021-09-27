# Generated by Django 3.2.6 on 2021-09-27 15:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resources', '0019_alter_note_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subject',
            name='sub_code',
            field=models.CharField(max_length=12),
        ),
        migrations.AddConstraint(
            model_name='subject',
            constraint=models.UniqueConstraint(fields=('sub_code', 'department'), name='unique_sub_code_per_department'),
        ),
    ]
