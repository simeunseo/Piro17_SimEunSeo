from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = "ideas"

urlpatterns = [
    path('', views.main, name='main'),
    path('register', views.register, name='register'),
    path('detail/<int:id>', views.detail, name='detail'),
    path('edit/<int:id>',views.edit, name="edit"),
    path('delete/<int:id>', views.delete, name="delete")
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)