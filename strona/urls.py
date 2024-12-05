from django.urls import path
from django.contrib import admin
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('blog', views.post_list, name='blog'),
    path('blog/<int:pk>/', views.post_detail, name='post_detail'),
    path('blog/new/', views.post_new, name='post_new'),
    path('blog/<int:pk>/edit/', views.post_edit, name='post_edit'),
    path('blog/<int:pk>/delete/', views.post_delete, name='post_delete'),
    path('blog/<int:blog_pk>/posts/new/', views.post_post_new, name='post_post_new'),
    path('blog/<int:blog_pk>/posts/<int:pk>/edit/', views.post_post_edit, name='post_post_edit'),
    path('blog/<int:blog_pk>/posts/<int:pk>/delete/', views.post_post_delete, name='post_post_delete'),
    path('about_us',views.about_us, name='about_us'),
    path('about_us/new/', views.about_us_new, name='about_us_new'),
    path('about_us/<int:pk>/edit/', views.about_us_edit, name='about_us_edit'),
    path('about_us/<int:pk>/delete/', views.about_us_delete, name='about_us_delete'),
    path('offers', views.offers, name='offers'),
    path('contact', views.contact, name='contact'),
    path('contact/email/', views.send_question_email_view, name='send_question_email_view'),

]