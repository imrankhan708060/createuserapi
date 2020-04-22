from rest_framework.routers import DefaultRouter
from core.api.views import CreateUserApi


router=DefaultRouter()
router.register("",CreateUserApi, basename='user')
urlpatterns = router.urls