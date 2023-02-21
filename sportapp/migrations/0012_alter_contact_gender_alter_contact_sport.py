# Generated by Django 4.0.1 on 2022-05-22 17:07

from django.db import migrations, models
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('sportapp', '0011_alter_contact_address_alter_contact_email_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='gender',
            field=models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('others', 'others')], default='', max_length=120),
        ),
        migrations.AlterField(
            model_name='contact',
            name='sport',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('Cricket', 'Cricket'), ('Kabaddi', 'Kabaddi'), ('Badmintion', 'Badmintion'), ('Chess', 'Chess'), ('Volleyball', 'Volleyball')], default='', max_length=120),
        ),
    ]
