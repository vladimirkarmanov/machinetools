# Generated by Django 3.0.6 on 2020-05-31 08:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('machinetools', '0003_auto_20200531_1247'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rigging',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Название')),
                ('description', models.TextField(max_length=2000, null=True, verbose_name='Описание')),
            ],
            options={
                'verbose_name': 'Оснастка',
                'verbose_name_plural': 'Оснастки',
            },
        ),
        migrations.CreateModel(
            name='RiggingType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Название')),
            ],
            options={
                'verbose_name': 'Вид оснастки',
                'verbose_name_plural': 'Виды оснасток',
            },
        ),
        migrations.CreateModel(
            name='RiggingImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='', verbose_name='Изображение')),
                ('rigging', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='machinetools.Rigging')),
            ],
            options={
                'verbose_name': 'Изображение оснастки',
                'verbose_name_plural': 'Изображения оснастки',
            },
        ),
        migrations.AddField(
            model_name='rigging',
            name='rigging_type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='machinetools.RiggingType', verbose_name='Вид оснастки'),
        ),
    ]