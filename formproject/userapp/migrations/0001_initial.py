# Generated by Django 5.1 on 2024-09-02 11:13

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, null=True)),
                ('price', models.IntegerField(null=True)),
                ('image', models.ImageField(upload_to='book_meadia')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='userapp.author')),
            ],
        ),
    ]
