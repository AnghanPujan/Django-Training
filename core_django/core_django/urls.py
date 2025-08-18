from django.contrib import admin
from django.urls import path, include
from home.views import home, about, contact, success_page
from vege.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
    path('success-page/', success_page, name='success_page'),
    path('recipe/', add_recipe, name='recipe'),
    path('student/',include('student.urls')),
    path('teacher/',include('teacher.urls'))
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)