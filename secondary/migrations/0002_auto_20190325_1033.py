# Generated by Django 2.2 on 2019-03-25 09:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('secondary', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Gender',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gender', models.CharField(max_length=30)),
            ],
            options={
                'verbose_name_plural': 'genders',
            },
        ),
        migrations.RemoveField(
            model_name='student',
            name='sex',
        ),
        migrations.AddField(
            model_name='student',
            name='Gender',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='secondary.Gender'),
        ),
    ]
