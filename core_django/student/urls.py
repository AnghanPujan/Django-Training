from django.urls import path
from student.views import all, single, register
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('all/',all, name='all'),
    path('single/', single, name='single'),
    path('register/', register, name='register')
]

if settings.DEBUG:  
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)