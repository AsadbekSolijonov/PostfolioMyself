# Generated by Django 4.2 on 2023-04-14 19:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0004_contactinfo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aboutme',
            name='pic',
            field=models.ImageField(upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='mywork',
            name='pic',
            field=models.ImageField(upload_to='images/'),
        ),
    ]
