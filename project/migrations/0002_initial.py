# Generated by Django 4.1.3 on 2023-08-24 19:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user', '0001_initial'),
        ('project', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='proposal',
            name='team',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.team'),
        ),
        migrations.AddField(
            model_name='project',
            name='proposal',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='project_proposal', to='project.proposal'),
        ),
        migrations.AddField(
            model_name='project',
            name='team',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='project_team', to='user.team'),
        ),
    ]
