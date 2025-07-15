from django.urls import path, include

from . import views

from rest_framework.authtoken.views import obtain_auth_token


urlpatterns = [
    # Main Page as HTML
    path('index', views.index, name="index"),

    # Menu API endpoints
    path('menu/', views.MenuItemView.as_view(), name="menu"),
    path('menu/<int:pk>', views.SingleMenuItemView.as_view(), name="single-menu-item-view"),

    # API token generation endpoint
    path('api-token-auth/', obtain_auth_token),

    # Protected Views
    path('message/', views.msg),
]
