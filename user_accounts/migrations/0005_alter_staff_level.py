# Generated by Django 4.1.7 on 2023-10-09 16:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_accounts', '0004_lectures_remove_product_referal_customer_email_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='staff',
            name='level',
            field=models.IntegerField(default=1),
        ),
    ]