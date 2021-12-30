# Generated by Django 4.0 on 2021-12-27 17:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('adminpannel', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomerCheckout',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_id', models.CharField(max_length=200)),
                ('payment_id', models.CharField(default=None, max_length=200, null=True)),
                ('total_amount', models.FloatField()),
                ('payment_signature', models.CharField(default=None, max_length=200, null=True)),
                ('reciept_num', models.CharField(max_length=200)),
                ('delivery_address', models.CharField(max_length=2000)),
                ('delivery_phone', models.CharField(max_length=20)),
                ('payment_complete', models.IntegerField(default=0)),
                ('payedon', models.DateTimeField(auto_now_add=True)),
                ('customer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='auth.user')),
            ],
        ),
        migrations.CreateModel(
            name='customerPayedProducts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=200)),
                ('price', models.FloatField()),
                ('product_description', models.CharField(max_length=1000)),
                ('checkout_details', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customer.customercheckout')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auth.user')),
            ],
        ),
        migrations.CreateModel(
            name='CustomerCart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('addedon', models.DateTimeField(auto_now_add=True)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auth.user')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adminpannel.products')),
            ],
        ),
    ]