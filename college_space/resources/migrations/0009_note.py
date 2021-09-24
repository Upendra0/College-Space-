# Generated by Django 3.2.6 on 2021-09-24 04:21

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import resources.models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_user_department'),
        ('resources', '0008_alter_subject_credit'),
    ]

    operations = [
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('topic', models.CharField(max_length=50)),
                ('file', models.FileField(upload_to=resources.models.notes_directory_path, validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['pdf'])])),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='resources.subject')),
                ('uploaded_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.contributor')),
            ],
        ),
    ]