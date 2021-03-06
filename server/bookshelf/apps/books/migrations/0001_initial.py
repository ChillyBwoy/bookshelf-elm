# Generated by Django 2.1.5 on 2019-01-16 10:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('isbn', models.CharField(blank=True, max_length=140, verbose_name='isbn')),
                ('title', models.CharField(max_length=140, verbose_name='title')),
                ('description', models.TextField(blank=True, verbose_name='description')),
                ('published_at', models.DateField(blank=True, null=True, verbose_name='publish date')),
            ],
        ),
    ]
