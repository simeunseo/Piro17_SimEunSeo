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
    path('delete/<int:id>', views.delete, name="delete"),
    path('tool',views.tool,name='tool'),
    path('tool/register',views.tool_register, name='tool_register'),
    path('tool/detail/<int:id>',views.tool_detail, name='tool_detail'),
    path('tool/edit/<int:id>',views.tool_edit,name="tool_edit"),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)