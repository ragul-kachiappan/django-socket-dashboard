from django.urls import path

from stats import consumers

websocket_urlpatterns = [
    path("ws/<str:dashboard_slug>/", consumers.DashboardConsumer.as_asgi())
]
