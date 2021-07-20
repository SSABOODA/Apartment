# Generated by Django 3.2.5 on 2021-07-19 11:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('admins', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Public',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=45, unique=True)),
                ('password', models.CharField(max_length=100)),
                ('household_number', models.CharField(max_length=10)),
                ('payment', models.DecimalField(decimal_places=3, default=0.0, max_digits=10)),
                ('admin', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='admins.admin')),
            ],
            options={
                'db_table': 'publics',
            },
        ),
    ]
