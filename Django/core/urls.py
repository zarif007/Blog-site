from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('blog_api.urls')),
    path('', include('blog.urls')),
    path('api/rest-auth/', include('rest_auth.urls')),
    path('api-auth/', include('rest_framework.urls')),
]
 