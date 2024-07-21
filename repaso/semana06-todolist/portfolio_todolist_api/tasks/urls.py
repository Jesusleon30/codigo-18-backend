from rest_framework.routers import DefaultRouter
from .views import CategoryViewSet, TaskViewSet



router = DefaultRouter()
#debemos registar las rutas
router.register(r'categories', CategoryViewSet)
router.register(r'tasks', TaskViewSet)

urlpatterns = router.urls
