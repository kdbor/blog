
from django.contrib import admin
from django.urls import path,include,re_path
from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [ 
    path('admin/', admin.site.urls),
    path('api/blog/',include(('blog_app.urls','blogs'),namespace='blogs')),
    path('api-auth/', include('rest_framework.urls')),
    path('tinymce/', include('tinymce.urls')),
    path('auth/', include('djoser.urls')),   #About Authentication
    path('auth/', include('djoser.urls.jwt')), #About Authentication
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += [
    re_path('^.*',TemplateView.as_view(template_name='index.html'))
    ]