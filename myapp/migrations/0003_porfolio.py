# Generated by Django 5.0.7 on 2024-07-16 13:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_about_img_content'),
    ]

    operations = [
        migrations.CreateModel(
            name='porfolio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Gallery', models.ImageField(upload_to='')),
            ],
        ),
    ]
