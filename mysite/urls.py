from django.urls import path
from django.contrib.auth import views
from django.views.generic.base import RedirectView

from django.conf import settings
from django.conf.urls.static import static

import strona.forms
import strona.views

from django.urls import include, re_path
from django.views.static import serve
from django.contrib import admin
admin.autodiscover()

urlpatterns = [
    path('', include('strona.urls')),
    path('accounts/login/', views.LoginView.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(next_page='/'), name='logout'),
    path('nimda/', admin.site.urls),
    re_path(r'^media/(?P<path>.*)$', serve,{'document_root': settings.MEDIA_ROOT}),
    re_path(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}),
    path('captcha/', include('captcha.urls')),

]

handler404 = 'strona.views.error_404_view'

if settings.DEBUG:
     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)