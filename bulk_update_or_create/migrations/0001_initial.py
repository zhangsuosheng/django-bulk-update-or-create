# Generated by Django 2.2.12 on 2020-05-29 20:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Lock',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('locked_by', models.TextField(blank=True, null=True)),
                ('expires_at', models.DateTimeField(blank=True, null=True)),
            ],
        ),
    ]