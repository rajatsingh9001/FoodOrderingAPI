# Generated by Django 3.2.9 on 2021-12-05 14:11

from django.db import migrations, models
import django.db.models.deletion
import phone_field.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254)),
                ('profile_picture', models.ImageField(upload_to='')),
                ('dob', models.DateTimeField()),
                ('mobile', phone_field.models.PhoneField(max_length=31)),
                ('address', models.TextField()),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], default='M', max_length=1)),
                ('nationality', models.CharField(max_length=20)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='MenuItems',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('category', models.CharField(max_length=50)),
                ('price', models.IntegerField()),
                ('description', models.TextField()),
                ('picture', models.ImageField(upload_to='')),
                ('prep_time', models.IntegerField()),
                ('is_veg', models.BooleanField()),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('is_available', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='RestaurantList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_picture', models.ImageField(upload_to='')),
                ('name', models.CharField(max_length=30)),
                ('address', models.TextField()),
                ('owner_name', models.CharField(max_length=30)),
                ('contact_person', models.CharField(max_length=30)),
                ('mobile', phone_field.models.PhoneField(blank=True, help_text='Contact phone number', max_length=31)),
                ('email', models.EmailField(max_length=254, null=True)),
                ('opening_time', models.TimeField(null=True)),
                ('closing_time', models.TimeField(null=True)),
                ('rating', models.IntegerField(null=True)),
                ('active', models.BooleanField(default=False)),
                ('disable', models.BooleanField(default=False)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('menu_list', models.TextField(default=None, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_time', models.DateTimeField(auto_now_add=True)),
                ('updated_time', models.DateTimeField(auto_now=True)),
                ('total_amount', models.IntegerField()),
                ('list_of_items', models.TextField(default=None, null=True)),
                ('customer_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='api.customer')),
                ('restaurant_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='api.restaurantlist')),
            ],
        ),
    ]