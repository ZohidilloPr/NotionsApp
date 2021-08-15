# Generated by Django 3.2.3 on 2021-07-18 01:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='NotionModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('aim', models.CharField(max_length=100)),
                ('about', models.TextField()),
                ('impt', models.BooleanField(default=False)),
                ('comp', models.BooleanField(default=False)),
                ('data', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]