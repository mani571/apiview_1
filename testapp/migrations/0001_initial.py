# Generated by Django 2.2 on 2021-06-17 12:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='details',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('position', models.CharField(max_length=10)),
                ('mobile', models.IntegerField()),
                ('address', models.TextField(max_length=50)),
            ],
            options={
                'db_table': 'DETAILS',
            },
        ),
    ]