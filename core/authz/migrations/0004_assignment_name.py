# Generated by Django 4.2.16 on 2024-10-24 17:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('authz', '0003_alter_classdata_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='assignment',
            name='name',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='class_int', to='authz.googleclass'),
        ),
    ]
