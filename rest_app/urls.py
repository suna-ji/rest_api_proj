from rest_framework.routers import DefaultRouter
from django.urls import include, path
from rest_app import views

# 라우터가 없다면?

router = DefaultRouter()
router.register('rest_app', views.PostViewSet)


urlpatterns = [
    path('', include(router.urls))
]