# Generated by Django 4.0.6 on 2022-07-12 10:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=20)),
                ('lname', models.CharField(max_length=20)),
                ('emp_sal', models.IntegerField()),
                ('email', models.CharField(default='123@gmail.com', max_length=40)),
            ],
        ),
    ]