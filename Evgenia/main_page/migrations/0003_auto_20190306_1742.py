# Generated by Django 2.1.7 on 2019-03-06 17:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_page', '0002_auto_20190306_1733'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articles',
            name='day_of_week',
            field=models.CharField(choices=[('Понедельник', 'Понедельник'), ('Вторник', 'Вторник'), ('Среда', 'Среда'), ('Четверг', 'Четверг'), ('Пятница', 'Пятница'), ('Суббота', 'Суббота')], default='Понедельник', max_length=20),
        ),
    ]
