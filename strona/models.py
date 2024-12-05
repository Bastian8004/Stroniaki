#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.utils import timezone
from django.db import models


class Blog(models.Model):
    Title = models.CharField(max_length=70, blank=True, null=True)
    Description = models.TextField(max_length=1024, blank=True, null=True)
    Photo = models.ImageField(upload_to='albums', blank=True, null=True)
    Left = models.BooleanField()
    Right = models.BooleanField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()
    def __str__(self):
        return self.Title if self.Title else 'Bez tytułu'

    def data(self):
        if self.created_date:
            return self.created_date.strftime('%d-%m-%Y, %H:%M')
        return "Brak daty"

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

class Post(models.Model):
    Blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    Title = models.CharField(max_length=70, blank=True, null=True, default="")
    Description = models.TextField(max_length=2048, blank=True, null=True)
    Photo = models.ImageField(upload_to='albums', blank=True, null=True)
    Left = models.BooleanField()
    Right = models.BooleanField()
    Middle = models.BooleanField()
    Empty = models.BooleanField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()
    def __str__(self):
        return self.Title if self.Title else ''

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)


class About_us(models.Model):
    Title = models.CharField(max_length=70, blank=True, null=True)
    Description = models.TextField(max_length=1024, blank=True, null=True)
    Photo = models.ImageField(upload_to='albums', blank=True, null=True)
    Left = models.BooleanField()
    Right = models.BooleanField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True,null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.Title


class Contact(models.Model):
    Factory = models.CharField(max_length=70,blank=True, null=True)
    Phone = models.CharField(max_length=70,blank=True, null=True)
    Email = models.CharField(max_length=70,blank=True, null=True)


class ContactForm(models.Model):
    Name = models.CharField(max_length=100,blank=True, null=True)
    Subject = models.CharField(max_length=200,blank=True, null=True)
    Phone = models.CharField(max_length=70,blank=True, null=True)
    Email = models.CharField(max_length=70,blank=True, null=True)
    Message = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)

    def send(self):
        self.created_date = timezone.now()
        self.save()


class Main(models.Model):
    Title = models.CharField(max_length=70, blank=True, null=True)
    Description = models.TextField(max_length=1024, blank=True, null=True)