from django.urls import path
from django.conf import settings
from django.contrib import admin
from django.views.generic import TemplateView
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name="index"),
    path('api/process-video/', views.process_video, name="process_video"),
    path('api/upload-video/', views.upload_video, name="upload_video"),
]

if not settings.DEBUG:
    urlpatterns += [
        path('', TemplateView.as_view(template_name='index.html')),
    ]
else:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
