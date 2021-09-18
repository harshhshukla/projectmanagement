# Generated by Django 3.2.7 on 2021-09-17 10:03

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('mainProjects', '0002_remarks'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('favmovie_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('PhoneNo', models.IntegerField()),
                ('Email', models.CharField(default='', max_length=50)),
                ('Descriptionn', models.CharField(default='', max_length=50)),
                ('pub_date', models.DateField(default=django.utils.timezone.now)),
            ],
        ),
    ]