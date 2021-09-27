# Generated by Django 3.2.6 on 2021-09-27 17:29

from django.db import migrations, models
import users.models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0010_alter_user_profile_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='profile_pic',
            field=models.ImageField(default='profile_pics/default.jpeg', upload_to=users.models.profile_directory_path, validators=[users.models.validate_image_size]),
        ),
    ]
