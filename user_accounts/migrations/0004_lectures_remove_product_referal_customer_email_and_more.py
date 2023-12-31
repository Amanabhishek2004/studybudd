# Generated by Django 4.1.7 on 2023-10-09 16:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('user_accounts', '0003_customer'),
    ]

    operations = [
        migrations.CreateModel(
            name='lectures',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('caption', models.CharField(max_length=25)),
            ],
        ),
        migrations.RemoveField(
            model_name='product',
            name='referal',
        ),
        migrations.AddField(
            model_name='customer',
            name='email',
            field=models.EmailField(max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='customer',
            name='email_is_verified',
            field=models.BooleanField(default=False, null=True),
        ),
        migrations.AddField(
            model_name='customer',
            name='email_token',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='craeted',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='product',
            name='price',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='version',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='staff',
            name='level',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.RemoveField(
            model_name='customer',
            name='Product_purchased',
        ),
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('razorpay_order_id', models.CharField(blank=True, max_length=20, null=True)),
                ('razorpay_payment_id', models.CharField(blank=True, max_length=20, null=True)),
                ('razorpay_payment_signature', models.CharField(blank=True, max_length=20, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('Course_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user_accounts.product')),
                ('Owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='customer',
            name='Product_purchased',
            field=models.ManyToManyField(to='user_accounts.product'),
        ),
    ]
