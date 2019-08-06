# Generated by Django 2.2.3 on 2019-08-06 13:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dishes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dish_name', models.TextField(verbose_name='Name of dish')),
            ],
            options={
                'verbose_name': 'dishes',
                'verbose_name_plural': 'dishes',
            },
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(upload_to='dishes', verbose_name='Photo')),
                ('dishes', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='photos', to='dishes.Dishes')),
            ],
            options={
                'verbose_name': 'photo',
                'verbose_name_plural': 'photos',
            },
        ),
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ingredient', models.CharField(choices=[('potatoes', 'Potatoes'), ('cucumber', 'Cucumber'), ('meat', 'Meat')], max_length=8, verbose_name='Ingredient')),
                ('quantitty', models.FloatField(verbose_name='Quantity (in gramms)')),
                ('origin', models.CharField(choices=[('local', 'Local'), ('non-local', 'Non-local')], max_length=9, verbose_name='Place of origin')),
                ('dishes', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ingredients', to='dishes.Dishes')),
            ],
            options={
                'verbose_name': 'ingredient',
                'verbose_name_plural': 'ingredients',
            },
        ),
    ]
