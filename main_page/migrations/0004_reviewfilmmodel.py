# Generated by Django 4.2.7 on 2023-11-28 02:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_page', '0003_slider'),
    ]

    operations = [
        migrations.CreateModel(
            name='ReviewFilmModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('review_text', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('film_list', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_page.filmmodel')),
            ],
        ),
    ]
