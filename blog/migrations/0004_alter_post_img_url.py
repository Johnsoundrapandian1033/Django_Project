# Generated by Django 5.1.6 on 2025-03-05 08:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_alter_post_img_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='img_url',
            field=models.URLField(null=True),
        ),
    ]
