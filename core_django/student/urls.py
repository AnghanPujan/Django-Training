from django.urls import path
from student.views import all, single, register,login
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('all/',all, name='all'),
    path('single/', single, name='single'),
    path('register/', register, name='register'),
    path('login/', login, name='login')
]

if settings.DEBUG:  
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)