# Generated by Django 3.2 on 2021-04-13 07:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('map', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='squirrel',
            old_name='fur_color',
            new_name='primary_fur_color',
        ),
        migrations.RenameField(
            model_name='squirrel',
            old_name='uni_squirrel_id',
            new_name='unique_squirrel_id',
        ),
        migrations.AlterField(
            model_name='squirrel',
            name='age',
            field=models.CharField(choices=[('Adult', 'Adult'), ('Juvenile', 'Juvenile')], help_text='Age is a choice between Adult and Juvenile', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='squirrel',
            name='date',
            field=models.DateField(help_text='Date', null=True),
        ),
        migrations.AlterField(
            model_name='squirrel',
            name='shift',
            field=models.CharField(choices=[('AM', 'AM'), ('PM', 'PM')], help_text='Shift', max_length=255),
        ),
    ]
