# Generated by Django 3.2 on 2022-03-18 03:00

import cloudinary.models
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Apartment',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('price', models.DecimalField(decimal_places=2, max_digits=8)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='AppName',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('apartment_name', models.CharField(choices=[('Tony', 'Tony Apartment for max4 people'), ('Matea', 'Matea apartment for max4 people'), ('Martina', 'Martina apartment for max6 people')], max_length=10)),
                ('front_image', cloudinary.models.CloudinaryField(default='first_img', max_length=255, verbose_name='front_image')),
                ('front_image2', cloudinary.models.CloudinaryField(default='second_img', max_length=255, verbose_name='front_image2')),
                ('front_image3', cloudinary.models.CloudinaryField(default='third_img', max_length=255, verbose_name='front_image3')),
                ('price', models.DecimalField(decimal_places=2, max_digits=8)),
                ('description', models.TextField(null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='AppStatus',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('status', models.CharField(max_length=20, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='GManager',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=25)),
                ('last_name', models.CharField(max_length=25)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Guest',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=30, unique=True)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('phone_number', models.CharField(max_length=20, unique=True)),
                ('password', models.CharField(max_length=20)),
                ('otp_code', models.CharField(max_length=6, null=True, unique=True)),
                ('email_verified', models.BooleanField(default=False)),
                ('is_admin', models.BooleanField(default=False)),
                ('is_superadmin', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='PaymentType',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('amount', models.CharField(max_length=10)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('guest_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bookingapp.guest')),
                ('manager_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bookingapp.gmanager')),
                ('payment_type_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bookingapp.paymenttype')),
            ],
        ),
        migrations.AddField(
            model_name='gmanager',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bookingapp.guest'),
        ),
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('apartment_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bookingapp.apartment')),
                ('guest_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bookingapp.guest')),
                ('manager_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bookingapp.gmanager')),
                ('payment_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bookingapp.payment')),
            ],
        ),
        migrations.AddField(
            model_name='apartment',
            name='app_name_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bookingapp.appname'),
        ),
        migrations.AddField(
            model_name='apartment',
            name='app_status_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bookingapp.appstatus'),
        ),
    ]
