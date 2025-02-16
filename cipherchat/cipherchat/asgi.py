import os
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from chat.routing import websocket_urlpatterns  # Import WebSocket routes

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'cipherchat.settings')  # Change to your project name

application = ProtocolTypeRouter({
    "http": get_asgi_application(),  # Handles HTTP requests
    "websocket": AuthMiddlewareStack(  # Handles WebSockets
        URLRouter(websocket_urlpatterns)
    ),
})
