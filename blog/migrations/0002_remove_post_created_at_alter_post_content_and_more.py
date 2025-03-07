# Generated by Django 5.1.6 on 2025-03-05 07:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='created_at',
        ),
        migrations.AlterField(
            model_name='post',
            name='content',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='post',
            name='img_url',
            field=models.URLField(blank=True, default=1),
            preserve_default=False,
        ),
    ]
