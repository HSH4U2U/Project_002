<<<<<<< HEAD
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('asitis/', include('asitis.urls')),
    path('notice_spider/', include('notice_spider.urls')),
]

=======
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('asitis/', include('asitis.urls')),
    path('notice_spider/', include('notice_spider.urls')),
]

>>>>>>> bfc488ad51715cf21e4e02fbe4765263f013a6aa
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)