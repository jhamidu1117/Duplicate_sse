from django.urls import include, path
from rest_framework import routers
from .views import TRGidViewSet, TRGsView


router = routers.DefaultRouter()
router.register(r'trg_ids', TRGidViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('trg-list/', TRGsView.as_view(), name='list')

]