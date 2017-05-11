# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-28 19:01
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(

            name='Character',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('race', models.CharField(choices=[(b'HM', b'Human'), (b'EL', b'Elf'), (b'OR', b'Orc'), (b'DW', b'Dwarf'), (b'WR', b'Werewolf')], max_length=3)),
                ('health', models.IntegerField(default=100)),
            ],
        ),
        
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('game_type', models.CharField(choices=[(b'SP', b'Simpleplay'), (b'MP', b'Multiplay')], max_length=3)),                ('data_begin', models.DateField(auto_now=True)),
                ('data_end', models.DateField(blank=True, null=True)),

            ],
        ),

        migrations.AddField(
             model_name='character',
             name='room',
             field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='room.Room'),
        ),
    ]
