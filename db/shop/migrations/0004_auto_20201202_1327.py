# Generated by Django 2.2.3 on 2020-12-02 13:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_auto_20201202_1034'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shop',
            name='toggle',
            field=models.CharField(blank=True, choices=[('gps', 'Użyj GPS / Use GPS'), ('interactive', 'Wybierz punkt na mapie / Point on Map'), ('manual', 'Wprowadzić ręcznie / Enter Manually')], max_length=11, null=True, verbose_name='Location Mode'),
        ),
    ]
