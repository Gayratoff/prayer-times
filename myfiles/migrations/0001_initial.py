# Generated by Django 4.1.1 on 2023-02-03 15:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Viloyatlar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('viloyat', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'Viloyatlar',
                'verbose_name_plural': 'Viloyatlar',
            },
        ),
        migrations.CreateModel(
            name='Citys',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('manzil', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myfiles.viloyatlar')),
            ],
            options={
                'verbose_name': 'Citys',
                'verbose_name_plural': 'Citys',
            },
        ),
    ]
