# Generated by Django 4.2.2 on 2023-07-28 19:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cards', '0013_alter_cardset_first_name_alter_cardset_last_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cardset',
            name='first_name',
            field=models.CharField(default='PlaceHolder_FirstName', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='cardset',
            name='last_name',
            field=models.CharField(default='PlaceHolder_LastName', max_length=100, null=True),
        ),
    ]