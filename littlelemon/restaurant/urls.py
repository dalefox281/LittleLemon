from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet, basename="users")

urlpatterns = [
    path('', include(router.urls)),
    path('index', views.index, name="index"),
    path('menu/', views.MenuItemView.as_view(), name="menu"),
    path('menu/<int:pk>', views.SingleMenuItemView.as_view(), name="single-menu-item-view"),
]
