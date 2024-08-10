# Generated by Django 5.1 on 2024-08-10 09:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_student_student_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='ImangeModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('original_image', models.ImageField(upload_to='images/')),
                ('thumbnail_small', models.ImageField(blank=True, null=True, upload_to='images/thumbnails')),
                ('thumbnail_medium', models.ImageField(blank=True, null=True, upload_to='images/thumbnails')),
                ('thumbnail_large', models.ImageField(blank=True, null=True, upload_to='images/thumbnails')),
            ],
        ),
        migrations.DeleteModel(
            name='Student',
        ),
    ]
