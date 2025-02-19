# Generated by Django 3.1.2 on 2021-04-02 06:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Educators',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('educator_name', models.CharField(default='', max_length=200)),
                ('educator_surname', models.CharField(default='', max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Students',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_name', models.CharField(default='', max_length=200)),
                ('student_surname', models.CharField(default='', max_length=200)),
            ],
        ),
    ]
