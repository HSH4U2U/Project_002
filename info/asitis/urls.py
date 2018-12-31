from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = "asitis"

urlpatterns = [
    path('', views.base, name="base"),
    path('detail/<int:pk>', views.detail, name="detail"),
    # path('like', views.comment_like, name='comment_like'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
