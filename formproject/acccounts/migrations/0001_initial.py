# Generated by Django 5.1 on 2024-09-02 10:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Logintable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=200)),
                ('fname', models.CharField(max_length=200)),
                ('lname', models.CharField(max_length=200)),
                ('password', models.CharField(max_length=200)),
                ('password2', models.CharField(max_length=200)),
                ('type', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Userproile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=200)),
                ('fname', models.CharField(max_length=200)),
                ('lname', models.CharField(max_length=200)),
                ('password', models.CharField(max_length=200)),
                ('password2', models.CharField(max_length=200)),
            ],
        ),
    ]
