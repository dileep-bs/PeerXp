# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone



departments=(
		('None','-None-'),
        ('PWSLab DevOps Support', 'PWSLab DevOps Support'),
        ('iSupport', 'iSupport'),
    )



categories=(
		('None','-None-'),
		('DevSecOps Pipeline Setup','DevSecOps Pipeline Setup'),
		('CI/CD pipeline failure','CI/CD pipeline failure'),
		('Automated Deployment failure','Automated Deployment failure'),
		('Docker and Containers','Docker and Containers'),
		('Kubernetes Deployments (like EKS/GCP)','Kubernetes Deployments (like EKS/GCP)'),
		('Git Source control','Git Source control'),
		('PWSLab server not responding (502/503 errors)','PWSLab server not responding (502/503 errors)'),
    	('NEW Project CI/CD Pipeline Setup','NEW Project CI/CD Pipeline Setup'),
    	('Update CI/CD Pipeline Configuration','Update CI/CD Pipeline Configuration'),
    )



priorities=(
		('None','-None-'),
        ('High - Production System Down', 'High - Production System Down'),
        ('Medium - System Impaired', 'Medium - System Impaired'),
        ('Low - General Guidance','Low - General Guidance'),
    )




class Ticket(models.Model):
    username= models.ForeignKey(User, on_delete=models.CASCADE)
    department=models.CharField(max_length=30,choices=departments)
    category=models.CharField(max_length=80,choices=categories)
    pwSLab_project_uRL= models.URLField(max_length=250, null=True, blank=False)
    subject=models.CharField(max_length=50)
    description=models.TextField(max_length=300)
    phone=models.CharField(max_length=13,blank=True)
    file=models.FileField(upload_to='files/%Y/%m/%d',blank=True)
    priority=models.CharField(max_length=30,choices=priorities)

	