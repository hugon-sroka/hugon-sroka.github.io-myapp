from django.urls import path
from django.conf import settings
from . import views
from django.conf.urls.static import static
from .views import PostListView


urlpatterns = [
    path('', PostListView.as_view(), name='blog-home'),
    path('about/', views.about, name="blog-about")
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


