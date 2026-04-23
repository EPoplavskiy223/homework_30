from django.urls import include, path
from rest_framework.routers import SimpleRouter

from users.apps import UsersConfig
from users.views import PaymentViewSet, UsersViewSet

app_name = UsersConfig.name

router = SimpleRouter()
router.register("user", UsersViewSet, basename="users")
router.register("payments", PaymentViewSet, basename="pay")

urlpatterns = [
    path("", include(router.urls)),
]
