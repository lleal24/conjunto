# Generated by Django 2.2.1 on 2019-06-03 03:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('conjunto', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Salon',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_salon', models.CharField(max_length=50)),
                ('estado', models.CharField(choices=[('S', 'Small'), ('S', 'Small')], max_length=1)),
                ('conjunto', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='conjunto.Conjunto')),
            ],
        ),
    ]
