# Generated by Django 2.0.5 on 2018-05-23 09:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='dateofbird',
            new_name='dateofbirth',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='email',
            new_name='gmailaddress',
        ),
        migrations.AddField(
            model_name='user',
            name='gender',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]
