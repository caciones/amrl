# Generated by Django 4.1.5 on 2023-01-22 21:32

import django.contrib.gis.db.models.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Point',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField()),
                ('text', models.TextField(blank=True, null=True)),
                ('sequence_number', models.IntegerField()),
                ('location', django.contrib.gis.db.models.fields.PointField(srid=4326)),
                ('speech_file', models.FileField(upload_to='speech/')),
            ],
        ),
        migrations.CreateModel(
            name='Writer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('birth_date', models.DateField()),
                ('nationality', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Route',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(unique=True)),
                ('city', models.TextField()),
                ('writer', models.ManyToManyField(to='amrl.writer')),
            ],
        ),
        migrations.CreateModel(
            name='PointImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('caption', models.TextField()),
                ('image', models.ImageField(null=True, upload_to='point/')),
                ('point', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='amrl.point')),
            ],
        ),
        migrations.AddField(
            model_name='point',
            name='route',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='amrl.route'),
        ),
        migrations.AlterUniqueTogether(
            name='point',
            unique_together={('route', 'sequence_number')},
        ),
    ]
