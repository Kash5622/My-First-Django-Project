# Generated by Django 4.0.3 on 2022-05-28 05:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shoptop', '0004_product_stock'),
    ]

    operations = [
        migrations.CreateModel(
            name='contact_us',
            fields=[
                ('contact_us_id', models.AutoField(primary_key=True, serialize=False)),
                ('fname', models.CharField(max_length=50)),
                ('lname', models.CharField(max_length=50)),
                ('uname', models.CharField(max_length=50)),
                ('eaddress', models.CharField(max_length=50)),
                ('tarea', models.CharField(max_length=500)),
            ],
        ),
    ]
