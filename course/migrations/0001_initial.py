# Generated by Django 4.1.1 on 2022-10-04 15:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('trainer', '0003_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Training',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('trainer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='trainer.trainer')),
            ],
        ),
    ]
