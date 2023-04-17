# Generated by Django 4.1.4 on 2023-04-17 10:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('rate', models.FloatField()),
                ('created_date', models.DateField(auto_now=True)),
                ('modified_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
