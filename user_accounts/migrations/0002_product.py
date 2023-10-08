# Generated by Django 4.1.7 on 2023-09-30 12:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user_accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
                ('referal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user_accounts.staff')),
            ],
        ),
    ]