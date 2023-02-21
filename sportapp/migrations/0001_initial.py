# Generated by Django 4.0.1 on 2022-04-02 10:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('email', models.CharField(max_length=120)),
                ('phone', models.CharField(max_length=120)),
                ('gender', models.CharField(choices=[('Cricket', 'Cricket'), ('Kabaddi', 'Kabbaddi'), ('Badmintion', 'Badmintion'), ('Chess', 'Chess'), ('Volleyball', 'volleyball')], max_length=120)),
                ('choose_sport', models.CharField(choices=[('Cricket', 'Cricket'), ('Kabaddi', 'Kabbaddi'), ('Badmintion', 'Badmintion'), ('Chess', 'Chess'), ('Volleyball', 'volleyball')], max_length=120)),
                ('address', models.CharField(max_length=120)),
                ('date', models.DateField()),
            ],
        ),
    ]
