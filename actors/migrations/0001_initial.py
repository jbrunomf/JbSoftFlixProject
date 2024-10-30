# Generated by Django 5.1.2 on 2024-10-30 01:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Actor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('birth_date', models.DateField(blank=True, null=True)),
                ('nationality', models.CharField(blank=True, choices=[('USA', 'United States'), ('UK', 'United Kingdom'), ('FR', 'France'), ('DE', 'Germany'), ('IT', 'Italy'), ('ES', 'Spain'), ('RU', 'Russia'), ('BR', 'Brazil'), ('CN', 'China'), ('IN', 'India')], default='BR', max_length=3, null=True)),
            ],
        ),
    ]
