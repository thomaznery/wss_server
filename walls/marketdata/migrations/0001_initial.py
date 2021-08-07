# Generated by Django 3.2.6 on 2021-08-06 00:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ContratoFuturo',
            fields=[
                ('codigo', models.CharField(max_length=11, primary_key=True, serialize=False)),
                ('ticket', models.CharField(max_length=7, unique=True)),
                ('vencimento', models.DateField()),
                ('status', models.IntegerField(choices=[(1, 'Atual'), (2, 'Vencido'), (3, 'Proximo')], default=2)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]