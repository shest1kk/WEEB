# Generated by Django 4.2 on 2023-05-03 14:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_alter_car_license_plate_alter_userprofile_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='user',
            new_name='lastName',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='firstName',
            field=models.CharField(default=12, max_length=32),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='rental',
            name='renter',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orders.userprofile'),
        ),
    ]