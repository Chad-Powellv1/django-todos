from django.conf.urls.static import static
from rest_framework import routers
from django.urls import path, include
from . import views

router = routers.DefaultRouter()
router.register(r'todo', views.TodoViewSet)
router.register(r'event', views.EventViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api/token/', TokenObtainPairView.as_View(),
    name = 'token_obtain_pair'),
    path('login', views.login_view),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)