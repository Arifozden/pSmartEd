# Generated by Django 5.0.1 on 2024-01-21 23:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Enter the course name', max_length=200, unique=True, verbose_name='Course Name')),
                ('description', models.TextField(blank=True, help_text='Enter the course description', null=True, verbose_name='Description')),
                ('image', models.ImageField(default='courses/default.jpg', help_text='Upload the course image', upload_to='courses/%Y/%m/%d/', verbose_name='Image')),
                ('date', models.DateTimeField(auto_now=True, help_text='Enter the date of the course', verbose_name='Date')),
                ('availabe', models.BooleanField(default=True, help_text='Check if the course is available', verbose_name='Available')),
            ],
        ),
    ]