# Generated by Django 5.1 on 2024-09-09 23:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quotes', '0007_remove_customuser_username_alter_customuser_email'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='customuser',
            options={'permissions': [('can_view_profile', 'Can view profile'), ('can_edit_profile', 'Can edit profile')]},
        ),
        migrations.AlterModelManagers(
            name='customuser',
            managers=[
            ],
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='date_joined',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='is_active',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='is_staff',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='last_name',
        ),
    ]
