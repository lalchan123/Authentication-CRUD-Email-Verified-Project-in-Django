# Generated by Django 3.0.5 on 2021-07-17 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth_crud_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('subject', models.CharField(max_length=250)),
                ('message', models.TextField()),
            ],
        ),
    ]
