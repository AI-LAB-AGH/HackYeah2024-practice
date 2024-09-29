from django.urls import path
from django.conf import settings
from django.contrib import admin
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name="index"),
    path('api/process-video/', views.process_video, name="process_video"),
    path('api/get-video/', views.serve_temp_file, name='get_video'),
    path('api/delete-video/', views.delete_video, name='delete_video'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
