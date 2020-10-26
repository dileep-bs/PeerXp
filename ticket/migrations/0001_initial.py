# Generated by Django 2.1.10 on 2020-10-23 13:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('department', models.CharField(choices=[('None', '-None-'), ('PWSLab DevOps Support', 'PWSLab DevOps Support'), ('iSupport', 'iSupport')], max_length=30)),
                ('category', models.CharField(choices=[('None', '-None-'), ('DevSecOps Pipeline Setup', 'DevSecOps Pipeline Setup'), ('CI/CD pipeline failure', 'CI/CD pipeline failure'), ('Automated Deployment failure', 'Automated Deployment failure'), ('Docker and Containers', 'Docker and Containers'), ('Kubernetes Deployments (like EKS/GCP)', 'Kubernetes Deployments (like EKS/GCP)'), ('Git Source control', 'Git Source control'), ('PWSLab server not responding (502/503 errors)', 'PWSLab server not responding (502/503 errors)'), ('NEW Project CI/CD Pipeline Setup', 'NEW Project CI/CD Pipeline Setup'), ('Update CI/CD Pipeline Configuration', 'Update CI/CD Pipeline Configuration')], max_length=80)),
                ('pwSLab_project_uRL', models.URLField(max_length=250, null=True)),
                ('subject', models.CharField(max_length=50)),
                ('description', models.TextField(max_length=300)),
                ('phone', models.CharField(max_length=13)),
                ('file', models.FileField(upload_to='files/%Y/%m/%d')),
                ('priority', models.CharField(choices=[('None', '-None-'), ('High - Production System Down', 'High - Production System Down'), ('Medium - System Impaired', 'Medium - System Impaired'), ('Low - General Guidance', 'Low - General Guidance')], max_length=30)),
                ('username', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
