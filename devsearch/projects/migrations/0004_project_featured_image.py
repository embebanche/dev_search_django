# Generated by Django 4.0.3 on 2022-03-31 12:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0003_rename_tag_project_tags'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='featured_image',
            field=models.ImageField(blank=True, default='default.jpg', null=True, upload_to=''),
        ),
    ]
